import streamlit as st
import pandas as pd

st.title("LatentAnalytics")

episode_df = pd.read_csv("data/exports/episodes.csv")
sentiment_df = pd.read_csv("data/processed/sentiment_comments.csv")

st.header("Episode Statistics")

st.dataframe(episode_df)

st.metric(
    "Views",
    f"{episode_df['views'].iloc[0]:,}"
)

st.metric(
    "Likes",
    f"{episode_df['likes'].iloc[0]:,}"
)

st.metric(
    "Comments",
    f"{episode_df['comments'].iloc[0]:,}"
)

st.header("Sentiment Distribution")

st.bar_chart(
    sentiment_df["sentiment"].value_counts()
)