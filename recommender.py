import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def tokens(text):
    return set(re.findall(r"[a-z]+", str(text).lower()))


def recommend(df, matrix, encode, category, min_price, max_price,
              query="", top_k=10, max_per_brand=3,
              w_sem=0.7, w_kw=0.2, w_price=0.1):
    # 1. Hard filters
    mask = (df.category == category) & (df.price >= min_price) & (df.price <= max_price)
    mask &= df.image_url.fillna("").str.len() > 0
    sub = df[mask]
    if sub.empty:
        return sub

    # 2. Semantic score
    q_vec = encode(f"{query} {category}".strip())
    sem = cosine_similarity(q_vec, matrix[sub.index.to_numpy()])[0]

    # 3. Keyword score
    q_tokens = tokens(query)
    if q_tokens:
        kw = np.array([len(q_tokens & tokens(t)) / len(q_tokens) for t in sub["text"]])
    else:
        kw = np.zeros(len(sub))

    # 4. Price fit (prefer the middle of the chosen range)
    mid = (min_price + max_price) / 2
    half = max((max_price - min_price) / 2, 1)
    price_fit = 1 - np.minimum(np.abs(sub.price.values - mid) / half, 1)

    ranked = sub.assign(score=w_sem * sem + w_kw * kw + w_price * price_fit) \
                .sort_values("score", ascending=False)

    # 5. Brand diversity
    out, count = [], {}
    for idx, row in ranked.iterrows():
        if count.get(row.brand, 0) >= max_per_brand:
            continue
        out.append(idx)
        count[row.brand] = count.get(row.brand, 0) + 1
        if len(out) == top_k:
            break
    return ranked.loc[out]
