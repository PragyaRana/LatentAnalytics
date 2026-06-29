import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="LatentAnalytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 LatentAnalytics")
st.subheader("Audience Engagement & Sentiment Analysis")

episode_df = pd.read_csv("data/exports/episodes.csv")
sentiment_df = pd.read_csv("data/processed/sentiment_comments.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👀 Views", f"{episode_df['views'].iloc[0]:,}")

with col2:
    st.metric("👍 Likes", f"{episode_df['likes'].iloc[0]:,}")

with col3:
    st.metric("💬 Comments", f"{episode_df['comments'].iloc[0]:,}")

st.divider()

st.subheader("Episode Information")

st.dataframe(episode_df)

st.divider()

st.subheader("Audience Sentiment")

sentiment_counts = sentiment_df["sentiment"].value_counts()

st.bar_chart(sentiment_counts)

st.subheader("Word Cloud")

st.image(
    "reports/wordcloud.png",
    use_container_width=True
)