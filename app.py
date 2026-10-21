from pathlib import Path

import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from recommender import recommend

st.set_page_config(page_title="Fashion Recommender", layout="wide")

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "models" / "finetuned-minilm"
DATA_PATH = ROOT / "data" / "processed" / "products.csv"
EMB_PATH = ROOT / "data" / "processed" / "embeddings.npy"

CATEGORIES = ["Saree"]


def to_group(category, title):
    """Map any label or title to Saree, Shirt or Kurti."""
    for text in (str(category).lower(), str(title).lower()):
        if "saree" in text or "sari" in text:
            return "Saree"
        if "kurti" in text or "kurta" in text:
            return "Kurti"
        if "shirt" in text:
            return "Shirt"
    return None


@st.cache_resource
def load_model():
    m = SentenceTransformer(str(MODEL_PATH))
    m.max_seq_length = 128
    return m


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    emb = np.load(EMB_PATH)
    assert len(df) == len(emb), "products.csv and embeddings.npy are out of sync"

    # Numeric price (handles "₹4,500", "Rs. 2,999", blanks).
    # Rows are NOT dropped, so the order still matches embeddings.npy.
    df["price"] = (
        df["price"].astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
        .replace("", np.nan)
        .astype(float)
    )

    # Collapse all labels into Saree / Shirt / Kurti
    df["category"] = [to_group(c, t) for c, t in zip(df["category"], df["title"])]

    df["image_url"] = df["image_url"].fillna("").astype(str)
    df["brand"] = df["brand"].fillna("").astype(str)
    df["source"] = df["source"].fillna("").astype(str)
    return df, emb


model = load_model()
df, emb = load_data()
encode = lambda text: model.encode([text], normalize_embeddings=True)

st.title("Fashion Recommender")
st.caption("Pick a category and budget, and we rank matching products from several brands.")

with st.sidebar:
    category = st.selectbox("Category", CATEGORIES)

    cat_df = df[df.category == category]
    cat_prices = cat_df["price"].dropna()

    if cat_prices.empty:
        st.warning("No priced products in this category.")
        price_min, price_max = 0, 0
    else:
        lo = int(cat_prices.min())
        hi = int(cat_prices.max()) + 1
        if lo >= hi:
            hi = lo + 1

        # Default: the middle 80% of prices, so the slider never starts collapsed
        default = (int(cat_prices.quantile(0.1)), int(cat_prices.quantile(0.9)))
        if default[0] >= default[1]:
            default = (lo, hi)

        price_min, price_max = st.slider(
            "Price range (₹)", lo, hi, default,
            step=max(1, (hi - lo) // 200),
            key=f"price_{category}",          # resets the slider when the category changes
        )
        st.caption(f"{len(cat_df)} products in this category (₹{lo:,} to ₹{hi:,})")

    query = st.text_input("Describe what you want (optional)",
                          placeholder="e.g. red silk, wedding, cotton, light weight")
    top_k = st.slider("Number of results", 3, 20, 9)
    per_brand = st.slider("Max per brand", 1, 5, 3)
    go = st.button("Recommend", type="primary")

if go:
    if price_min >= price_max:
        st.warning("The price range is empty. Drag the right handle of the price slider to the right.")
    else:
        res = recommend(df, emb, encode, category, price_min, price_max,
                        query=query, top_k=top_k, max_per_brand=per_brand)
        if res.empty:
            st.warning("No products in this range. Try widening the price range.")
        else:
            cols = st.columns(3)
            for i, (_, r) in enumerate(res.iterrows()):
                with cols[i % 3]:
                    try:
                        st.image(r.image_url)
                    except Exception:
                        st.write("Image not available")
                    st.markdown(f"**{r.title}**")
                    st.write(f"₹{int(r.price):,} · {r.brand}")
                    label = "Instagram post" if r.source == "instagram" else "View product"
                    st.markdown(f"[{label}]({r.product_url})")
                    st.caption(f"Match: {r.score:.2f}")
else:
    st.info("Choose a category and price range in the sidebar, then click Recommend.")
