import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

files = {
    "2022/23": "E0_2223.csv",
    "2023/24": "E0_2324.csv",
    "2024/25": "E0_2425.csv",
    "2025/26": "E0_2526.csv"
}

frames = []

for season, filename in files.items():
    file_path = RAW_DIR / filename
    df = pd.read_csv(file_path)

    df["Season"] = season

    frames.append(df)

matches = pd.concat(frames, ignore_index=True)

match_columns = [
    "Season",
    "Date",
    "Time",
    "HomeTeam",
    "AwayTeam",
    "FTHG",
    "FTAG",
    "FTR",
    "HTHG",
    "HTAG",
    "HTR",
    "HS",
    "AS",
    "HST",
    "AST",
    "HF",
    "AF",
    "HC",
    "AC",
    "HY",
    "AY",
    "HR",
    "AR"
]

matches = matches[match_columns]

matches["Date"] = pd.to_datetime(
    matches["Date"],
    dayfirst=True,
    errors="coerce"
)

print("\n--- Missing Values ---")
print(matches.isna().sum()[matches.isna().sum() > 0])

print("\n--- Duplicate Rows ---")
print("Duplicate rows:", matches.duplicated().sum())

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

output_path = PROCESSED_DIR / "matches_clean.csv"

matches.to_csv(output_path, index=False)

print("\n--- Cleaning Complete ---")
print("Rows:", len(matches))
print("Columns:", len(matches.columns))
print("Saved to:", output_path)