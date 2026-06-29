import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/sentiment_comments.csv"
)

counts = df["sentiment"].value_counts()

plt.figure(figsize=(6,4))
counts.plot(kind="bar")

plt.title("Sentiment Distribution")

plt.tight_layout()

plt.savefig(
    "reports/sentiment_distribution.png"
)

plt.show()