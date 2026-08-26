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

youtube["EngagementRate"] = youtube["Engagement"].div(
    youtube["viewCount"].replace(0, pd.NA)
)

def assign_season(date):
    if date.month >= 8:
        return f"{date.year}/{str(date.year + 1)[-2:]}"
    else:
        return f"{date.year - 1}/{str(date.year)[-2:]}"

youtube["Season"] = youtube["publishedAt"].apply(assign_season)

matches_output = PROCESSED_DIR / "matches_analytics.csv"
youtube_output = PROCESSED_DIR / "youtube_analytics.csv"

matches.to_csv(
    matches_output,
    index=False
)

youtube.to_csv(
    youtube_output,
    index=False
)

print("\n--- Analytics Dataset Complete ---")
print("Match analytics:", matches_output)
print("YouTube analytics:", youtube_output)

