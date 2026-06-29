import pandas as pd
from textblob import TextBlob

df = pd.read_csv("data/processed/clean_comments.csv")

def get_sentiment(text):

    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"

    elif polarity < 0:
        return "Negative"

    else:
        return "Neutral"

df["sentiment"] = df["clean_comment"].apply(get_sentiment)

print(df["sentiment"].value_counts())

df.to_csv(
    "data/processed/sentiment_comments.csv",
    index=False
)