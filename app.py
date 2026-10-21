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

    # Make price numeric (handles "₹4,500", "Rs. 2,999", plain numbers, blanks).
    # Rows are NOT dropped, so the order still matches embeddings.npy.
    df["price"] = (
        df["price"].astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
        .replace("", np.nan)
        .astype(float)
    )

    # Clean text columns used by the filters and the cards
    df["category"] = df["category"].astype(str).str.strip()
    df["image_url"] = df["image_url"].fillna("").astype(str)
    df["brand"] = df["brand"].fillna("").astype(str)
    df["source"] = df["source"].fillna("").astype(str)
    return df, emb


model = load_model()
df, emb = load_data()
encode = lambda text: model.encode([text], normalize_embeddings=True)

st.title("Fashion Recommender")
st.caption("Pick a category and budget, and we rank matching products from several brands.")

CATEGORIES = ["Cotton Saree", "Kanchi Saree", "Fancy Saree", "Silk Saree", "Shirts", "Kurtis"]

with st.sidebar:
    category = st.selectbox("Category", CATEGORIES)
    price_min, price_max = st.slider("Price range (₹)", 0, 50000, (500, 8000), step=500)
    query = st.text_input("Describe what you want (optional)", placeholder="e.g. red bridal, light weight")
    top_k = st.slider("Number of results", 3, 20, 9)
    per_brand = st.slider("Max per brand", 1, 5, 3)
    go = st.button("Recommend", type="primary")

if go:
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
