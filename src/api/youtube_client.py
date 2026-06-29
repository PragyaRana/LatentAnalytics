from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

print("YouTube Client Connected")