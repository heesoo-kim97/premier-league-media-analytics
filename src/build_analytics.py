import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

PROCESSED_DIR = BASE_DIR / "data" / "processed"

matches = pd.read_csv(
    PROCESSED_DIR / "matches_clean.csv"
)

youtube = pd.read_csv(
    PROCESSED_DIR / "youtube_clean.csv"
)

print("Matches:", len(matches))
print("YouTube videos:", len(youtube))

matches["Date"] = pd.to_datetime(matches["Date"])

youtube["publishedAt"] = pd.to_datetime(
    youtube["publishedAt"]
)

youtube["Date"] = youtube["publishedAt"].dt.date
matches["Date"] = matches["Date"].dt.date

matches["TotalGoals"] = (
    matches["FTHG"] + matches["FTAG"]
)

matches["TotalShots"] = (
    matches["HS"] + matches["AS"]
)

matches["TotalShotsOnTarget"] = (
    matches["HST"] + matches["AST"]
)

matches["HighScoringMatch"] = (
    matches["TotalGoals"] >= 4
)

youtube["Engagement"] = (
    youtube["likeCount"] +
    youtube["commentCount"]
)

youtube["EngagementRate"] = (
    youtube["Engagement"] /
    youtube["viewCount"]
)