import pandas as pd
import re
import os

df = pd.read_csv("data/raw/comments/comments.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()

df["clean_comment"] = df["comment"].apply(clean_text)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/clean_comments.csv",
    index=False
)

print("Saved Successfully")
print(df.head())