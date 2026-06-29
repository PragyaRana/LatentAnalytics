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

response = youtube.commentThreads().list(
    part="snippet",
    videoId=VIDEO_ID,
    maxResults=100
).execute()

comments = []

for item in response["items"]:

    comment = item["snippet"]["topLevelComment"]["snippet"]

    comments.append({
        "author": comment["authorDisplayName"],
        "comment": comment["textDisplay"],
        "likes": comment["likeCount"]
    })

df = pd.DataFrame(comments)

os.makedirs("data/raw/comments", exist_ok=True)

df.to_csv(
    "data/raw/comments/comments.csv",
    index=False
)

print(df.head())
print(f"\nTotal Comments Fetched: {len(df)}")