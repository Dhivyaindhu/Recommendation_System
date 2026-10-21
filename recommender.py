import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def tokens(text):
    return set(re.findall(r"[a-z]+", str(text).lower()))


def recommend(df, matrix, encode, category, query="", top_k=10,
              max_per_brand=3, w_sem=0.8, w_kw=0.2):
    # 1. Filter by category (and skip rows with no image)
    mask = (df.category == category) & (df.image_url.fillna("").str.len() > 0)
    sub = df[mask]
    if sub.empty:
        return sub

    # 2. Semantic score
    q_vec = encode(f"{query} {category}".strip())
    sem = cosine_similarity(q_vec, matrix[sub.index.to_numpy()])[0]

    # 3. Keyword score: share of query words found in the product text
    q_tokens = tokens(query)
    if q_tokens:
        kw = np.array([len(q_tokens & tokens(t)) / len(q_tokens) for t in sub["text"]])
    else:
        kw = np.zeros(len(sub))

    ranked = sub.assign(score=w_sem * sem + w_kw * kw) \
                .sort_values("score", ascending=False)

    # 4. Brand diversity
    out, count = [], {}
    for idx, row in ranked.iterrows():
        if count.get(row.brand, 0) >= max_per_brand:
            continue
        out.append(idx)
        count[row.brand] = count.get(row.brand, 0) + 1
        if len(out) == top_k:
            break
    return ranked.loc[out]
