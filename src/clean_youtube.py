import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

file_path = RAW_DIR / "premier_league_youtube.xlsx"

youtube = pd.read_excel(
    RAW_DIR / "premier_league_youtube.xlsx",
    sheet_name="Premier League"
)

youtube_columns = [
    "videoId",
    "channelTitle",
    "videoTitle",
    "publishedAt",
    "videoCategoryLabel",
    "durationSec",
    "viewCount",
    "likeCount",
    "commentCount",
    "tags"
]

youtube = youtube[youtube_columns]

youtube["publishedAt"] = pd.to_datetime(
    youtube["publishedAt"],
    errors="coerce"
)

numeric_columns = [
    "durationSec",
    "viewCount",
    "likeCount",
    "commentCount"
]

for column in numeric_columns:
    youtube[column] = pd.to_numeric(
        youtube[column],
        errors="coerce"
    )

youtube = youtube.drop_duplicates(
    subset="videoId"
)

print("\n--- YouTube Data Check ---")
print("Channel titles:")
print(youtube["channelTitle"].value_counts())

print("\nFirst 5 videos:")
print(
    youtube[["channelTitle", "videoTitle"]]
    .head()
    .to_string(index=False)
)

print("\n--- Missing Values ---")
print(youtube.isna().sum()[youtube.isna().sum() > 0])

print("\n--- Duplicate Videos ---")
print(
    "Duplicate videos:",
    youtube["videoId"].duplicated().sum()
)

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

output_path = PROCESSED_DIR / "youtube_clean.csv"

youtube.to_csv(
    output_path,
    index=False
)

print("\n--- YouTube Cleaning Complete ---")
print("Rows:", len(youtube))
print("Columns:", len(youtube.columns))
print("Saved to:", output_path)