from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

VIDEO_ID = "eHTXQW58WhA"

response = youtube.videos().list(
    part="snippet,statistics",
    id=VIDEO_ID
).execute()

video = response["items"][0]

data = {
    "video_id": VIDEO_ID,
    "title": video["snippet"]["title"],
    "published_date": video["snippet"]["publishedAt"],
    "channel": video["snippet"]["channelTitle"],
    "views": int(video["statistics"].get("viewCount", 0)),
    "likes": int(video["statistics"].get("likeCount", 0)),
    "comments": int(video["statistics"].get("commentCount", 0)),
    "season": 2,
    "episode": 1
}

df = pd.DataFrame([data])

os.makedirs("data/exports", exist_ok=True)

df.to_csv(
    "data/exports/episodes.csv",
    index=False
)

print(df)

print("\nCSV Saved Successfully!")
print(os.path.abspath("data/exports/episodes.csv"))

df["engagement_rate"] = (
    (df["likes"] + df["comments"])
    / df["views"]
) * 100 