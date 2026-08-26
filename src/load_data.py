import pandas as pd
from pathlib import Path


RAW_DATA = Path("data/raw")


def load_match_data():
    seasons = {
        "2022/23": "E0_2223.csv",
        "2023/24": "E0_2324.csv",
        "2024/25": "E0_2425.csv",
        "2025/26": "E0_2526.csv",
    }

    matches = []

    for season, filename in seasons.items():
        filepath = RAW_DATA / filename
        df = pd.read_csv(filepath)
        df["Season"] = season
        matches.append(df)

    return pd.concat(matches, ignore_index=True)


def load_youtube_data():
    filepath = RAW_DATA / "premier_league_youtube.xlsx"

    return pd.read_excel(filepath)


if __name__ == "__main__":
    matches = load_match_data()
    youtube = load_youtube_data()

    print("Match records:", len(matches))
    print("YouTube records:", len(youtube))

