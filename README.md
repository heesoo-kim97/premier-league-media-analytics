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

Premier League YouTube video metadata containing information such as:

- Video title
- Publication date
- View count
- [INSERT OTHER AVAILABLE FIELDS]

---

## Data Preparation

Python was used to clean, validate, and prepare the datasets before loading them into MySQL.

### Match Data

The match datasets were combined and standardized across seasons.

Key preparation steps included:

- Combining season-level CSV files
- Standardizing column names
- Parsing match dates
- Standardizing team names
- Removing duplicate records
- Checking missing values
- Removing betting-related fields
- Creating consistent season identifiers
- Validating match result categories

### Data Quality Checks

The final match dataset contained:

- **1,520 rows**
- **23 columns**
- **0 duplicate rows**
- **0 missing values**

### Example Python Cleaning Code

```python
import pandas as pd

# Load season files
df_22 = pd.read_csv("../data/raw/premier_league_2022_23.csv")
df_23 = pd.read_csv("../data/raw/premier_league_2023_24.csv")
df_24 = pd.read_csv("../data/raw/premier_league_2024_25.csv")
df_25 = pd.read_csv("../data/raw/premier_league_2025_26.csv")

# Add season identifier
df_22["Season"] = "2022/23"
df_23["Season"] = "2023/24"
df_24["Season"] = "2024/25"
df_25["Season"] = "2025/26"

# Combine datasets
matches = pd.concat(
    [df_22, df_23, df_24, df_25],
    ignore_index=True
)

# Parse dates
matches["Date"] = pd.to_datetime(
    matches["Date"],
    dayfirst=True
)

# Remove duplicate rows
matches = matches.drop_duplicates()

# Check missing values
print(matches.isnull().sum())

# Check number of records
print(matches.shape)

# Save cleaned dataset
matches.to_csv(
    "../data/processed/premier_league_matches_clean.csv",
    index=False
)
