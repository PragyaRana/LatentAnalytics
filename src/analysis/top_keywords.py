import pandas as pd
from collections import Counter

df = pd.read_csv("data/processed/clean_comments.csv")

df = df.dropna(subset=["clean_comment"])

text = " ".join(df["clean_comment"])
words = text.split()

stopwords = {
    "the","is","a","an","and","to","of",
    "in","for","this","that","it","on",
    "with","i","you","samay","raina"
}

words = [w for w in words if w not in stopwords and len(w) > 2]

top_words = Counter(words).most_common(20)

for word, count in top_words:
    print(word, count)