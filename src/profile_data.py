import pandas as pd

from load_data import load_match_data, load_youtube_data


def profile_matches(df):
    print("\n" + "=" * 60)
    print("PREMIER LEAGUE MATCH DATA")
    print("=" * 60)

    print("\n--- Shape ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n--- Matches by Season ---")
    print(df["Season"].value_counts().sort_index())

    print("\n--- Columns ---")
    print(df.columns.tolist())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    missing = df.isnull().sum()
    print(missing[missing > 0].sort_values(ascending=False))

    print("\n--- Duplicate Rows ---")
    print(f"Duplicate rows: {df.duplicated().sum()}")

    print("\n--- Home Teams ---")
    print(df["HomeTeam"].value_counts())

    print("\n--- Away Teams ---")
    print(df["AwayTeam"].value_counts())


def profile_youtube(df):
    print("\n" + "=" * 60)
    print("YOUTUBE DATA")
    print("=" * 60)

    print("\n--- Shape ---")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n--- Columns ---")
    print(df.columns.tolist())

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    missing = df.isnull().sum()
    print(missing[missing > 0].sort_values(ascending=False))

    print("\n--- Duplicate Rows ---")
    print(f"Duplicate rows: {df.duplicated().sum()}")

    print("\n--- First 5 Rows ---")
    print(df.head())


if __name__ == "__main__":
    matches = load_match_data()
    youtube = load_youtube_data()

    profile_matches(matches)
    profile_youtube(youtube)