import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

files = {
    "2022/23": "EO_2223.csv",
    "2023/24": "EO_2324.csv",
    "2024/25": "EO_2425.csv",
    "2025/26": "EO_2526.csv"
}

frames = []

for season, filename in files.items():
    file_path = RAW_DIR / filename
    df = pd.read_csv(file_path)

    df["Season"] = season

    frames.append(df)

matches = pd.concat(frames, ignore_index=True)