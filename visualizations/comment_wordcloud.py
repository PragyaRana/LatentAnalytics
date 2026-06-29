import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/clean_comments.csv")

df = df.dropna(subset=["clean_comment"])

text = " ".join(df["clean_comment"])

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("India's Got Latent S2 EP1 Comment Word Cloud")

plt.savefig(
    "reports/wordcloud.png",
    bbox_inches="tight"
)

plt.show()