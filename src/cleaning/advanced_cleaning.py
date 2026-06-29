# src/cleaning/advanced_cleaning.py

import pandas as pd
import re

df = pd.read_csv("data/raw/comments/comments.csv")

df = df.drop_duplicates(subset=["comment"])

df = df.dropna()

df["comment_length"] = df["comment"].astype(str).apply(len)

df["word_count"] = df["comment"].astype(str).apply(
    lambda x: len(x.split())
)

df.to_csv(
    "data/processed/final_comments.csv",
    index=False
)
