import pandas as pd

df = pd.read_csv(
    "data/processed/clean_comments.csv"
)

text = " ".join(
    df["clean_comment"].astype(str)
).lower()

guests = {
    "Alia": text.count("alia"),
    "Sharvari": text.count("sharvari"),
    "Ashish": text.count("ashish")
}

guest_df = pd.DataFrame(
    guests.items(),
    columns=["Guest","Mentions"]
)

print(guest_df)

guest_df.to_csv(
    "data/processed/guest_mentions.csv",
    index=False
)