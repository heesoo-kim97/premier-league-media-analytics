# Premier League Media Analysis

> Analyzing Premier League match performance, content production, and digital engagement to identify trends and potential media opportunities.

<br>

![Python](https://img.shields.io/badge/Python-Data%20Preparation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Analysis-F29111?style=for-the-badge&logo=mysql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![VS%20Code](https://img.shields.io/badge/VS%20Code-Development-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Case](#business-case)
- [Business Questions](#business-questions)
- [Data Sources](#data-sources)
- [Data Preparation](#data-preparation)
- [Database Structure](#database-structure)
- [SQL Analysis](#sql-analysis)
- [Python Analysis](#python-analysis)
- [Key Findings](#key-findings)
- [Business Recommendations](#business-recommendations)
- [Visual Analysis](#visual-analysis)
- [Project Structure](#project-structure)
- [How to Reproduce](#how-to-reproduce)
- [Skills Demonstrated](#skills-demonstrated)

---

## Project Overview

This project analyzes the relationship between **Premier League match performance** and **digital media activity**.

The analysis combines:

- Premier League match results from the 2022/23–2025/26 seasons
- Premier League YouTube video metadata
- Match performance metrics
- YouTube publishing activity
- Video viewership metrics

The goal is to understand how football performance and digital content activity have changed over time and identify potential opportunities for sports media strategy.

### Project Scope

| Area | Coverage |
|---|---|
| Premier League Matches | 2022/23–2025/26 |
| Matches Analyzed | 1,520 |
| YouTube Data | [INSERT DATE RANGE] |
| Primary Tools | Python, SQL, MySQL |
| Visualization | [INSERT LATER] |

---

## Business Case

Imagine a U.S.-based sports media organization looking to better understand Premier League audience behavior.

The organization wants to answer questions such as:

- How has Premier League match performance changed?
- How much content is being produced?
- How has digital engagement changed?
- Are certain periods associated with higher audience interest?
- What types of content appear to generate the strongest engagement?

By combining match and digital media data, analysts can identify trends that may help inform:

- Content planning
- Promotional campaigns
- Audience engagement strategies
- Media programming
- Commercial opportunities

> **Important:** This analysis identifies relationships and trends in the data. It does not assume that match performance directly causes changes in YouTube engagement.

---

## Business Questions

### Match Performance

1. How many Premier League matches were analyzed in each season?
2. How has average goals per match changed across seasons?
3. How has the distribution of home wins, draws, and away wins changed?

### Digital Content

4. How many Premier League YouTube videos were published each year?
5. How has average video engagement changed over time?
6. Which videos generated the highest number of views?
7. Is video length associated with higher or lower view counts?

### Match Performance + Digital Engagement

8. Are seasons with higher-scoring matches associated with greater digital engagement?
9. Does increased match activity correspond with increased YouTube publishing activity?
10. What patterns in the data could help inform future sports media content strategy?

---

## Data Sources

### Premier League Match Data

The data was retrieved from [Football-Data.co](https://www.football-data.co.uk/englandm.php).

Match-level Premier League data covering the:

- 2022/23 season
- 2023/24 season
- 2024/25 season
- 2025/26 season

The dataset contains match information such as:

- Match date
- Home team
- Away team
- Full-time home goals
- Full-time away goals
- Match result
- Additional match-level statistics

Betting-related fields were excluded from the analysis because they were outside the scope of the business questions.

### YouTube Data

The data was retrieved from [Zenodo](https://zenodo.org/records/20719982).

Premier League YouTube video metadata containing information such as:

- Video title
- Publication date
- View count
- Video ID
- Video length
- Video description
- Video tag
- Video category

---

## Data Preparation

Python was used to prepare the Premier League match and YouTube datasets before analysis in MySQL. The workflow was designed to create consistent, validated datasets while keeping the original raw data unchanged.

The preparation process followed four main stages:

Load -> Profile -> Clean -> Build Analytics Dataset

### Data Preparation Workflow

#### 1. Loading the Raw Data

The project uses two primary data sources:
| Dataset                | Source Format | Coverage        | Purpose                                |
| ---------------------- | ------------- | --------------- | -------------------------------------- |
| Premier League Matches | CSV           | 2022/23–2025/26 | Match performance analysis             |
| Premier League YouTube | Excel         | 2022/23–2025/26 | Media and audience engagement analysis |


The four Premier League season files were loaded and combined into a single match dataset. A Season field was added during the loading process so each match could be assoiciated with its respective season.

The YouTube dataset was loaded separately from the Excel workbook.

<details>
    <summary>
        Python - Loading and combining season data:
    </summary>
    
```Python
seasons = {
    "2022/23": "E0_2223.csv",
    "2023/24": "E0_2324.csv",
    "2024/25": "E0_2425.csv",
    "2025/26": "E0_2526.csv"
}

```  
</details>

The full loading logic is contained in [src/load_data.py](https://github.com/heesoo-kim97/premier-league-media-analytics/blob/main/src/load_data.py).

#### 2. Data Profiling

Before cleaning, Python was used to profile both datasets and identify potential data-quality issues.

The profiling process examined:
- Dataset dimensions
- Column names
- Data types
- Missing values
- Duplicate records
- Match counts by season
- Home and away team distributions
- YouTube channel distribution
- Sample records

This allowed the cleaning process to be based on the actual structure and quality of the data rather than assimptions about the source files.

<details>
    <summary>
        Python - Profiling missing values and duplicates:
    </summary>
    
```Python
missing = df.isnull().sum()

print(missing[missing > 0])
print("Duplicate rows:", df.duplicated().sum())

```  
</details>

The full profiling logic is contained in [src/profile_data.py](https://github.com/heesoo-kim97/premier-league-media-analytics/blob/main/src/profile_data.py).

#### 3. Match Data Cleaning

The four season-level match files were combined into one consistent dataset.

The cleaning process included:
- Combining all four seasons
- Adding a consistent SEASON identifier
- Selecting only fields required for analysis
- Parsing match dates into a consistent datetime format
- Checking for missing values
- Checking for duplicate records
- Preserving match-level performance statistics

The final analytical match dataset contains 23 columns, covering match information, scores, results, shots, cards, and corners.

<b>Match Variables</b>

<details>
    <summary>
        Selected fields:
    </summary>    

```
Season
Date
Time
HomeTeam
AwayTeam
FTHG / FTAG
FTR
HTHG / HTAG
HTR
HS / AS
HST / AST
HF / AF
HC / AC
HY / AY
HR / AR
```  
</details>

This approach also removes source filds that were not required for the analysis, including the betting-related variables present in the original dataset.

<details>
    <summary>
        Python — Selecting analytical match fields:
    </summary>

```python
match_columns = [
    "Season", "Date", "Time",
    "HomeTeam", "AwayTeam",
    "FTHG", "FTAG", "FTR",
    ...
]

matches = matches[match_columns]
```
</details>

The complete field selection and cleaning is defined in [src/clean_matches.py](https://github.com/heesoo-kim97/premier-league-media-analytics/blob/main/src/clean_matches.py).

#### 4. YouTube Data Cleaning

The YouTube dataset was processed separately because its structure and data types differed from the match dataset.

The cleaning process included:
- Selecting relevant video fields
- Parsing publication timestamps
- Converting engagement metrics to numeric values
- Removing duplicate videos using videoId
- Standardizing text fields
- Checking missing values
- Validating channel and video records

The selected fields capture both video metadata and audience engagement.

<details>
    <summary>
        Selected fields:
    </summary>    

```
videoId
channelTitle
videoTitle
publishedAt
videoCategoryLabel
durationSec
viewCount
likeCount
commentCount
tags
```
</details>

This approach also removes source filds that were not required for the analysis, including the betting-related variables present in the original dataset.

<details>
    <summary>
        Python - Selecting analytical match fields:
    </summary>

    ```python
    match_columns = [
    "Season", "Date", "Time",
    "HomeTeam", "AwayTeam",
    "FTHG", "FTAG", "FTR",
    ---
]

matches = matches[match_columns]
    ```
</details>

The complete field selection is defined in [src/clean_matches.py](https://github.com/heesoo-kim97/premier-league-media-analytics/blob/main/src/clean_matches.py).

#### 5. Data Standardization

Match dates were converted into a consistent datetime format so they could be relianily used for analysis and later joined with the YouTube dataset.

```python
matches["Date"] = pd.to_datetime(matches["Date"])

youtube["publishedAt"] = pd.to_datetime(
    youtube["publishedAt"]
)

youtube["Date"] = youtube["publishedAt"].dt.date
matches["Date"] = matches["Date"].dt.date
```
