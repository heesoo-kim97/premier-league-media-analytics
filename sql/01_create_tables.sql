CREATE DATABASE IF NOT EXISTS premier_league_media;
USE premier_league_media;

CREATE TABLE matches (
    Season VARCHAR(10),
    Date DATE,
    Time TIME,
    HomeTeam VARCHAR(50),
    AwayTeam VARCHAR(50),
    FTHG INT,
    FTAG INT,
    FTR VARCHAR(1),
    HTHG INT,
    HTAG INT,
    HTR VARCHAR(1),
    HS INT,
    AS_ INT,
    HST INT,
    AST INT,
    HF INT,
    AF INT,
    HC INT,
    AC INT,
    HY INT,
    AY INT,
    HR INT,
    AR INT
);

CREATE TABLE youtube_videos (
    videoId VARCHAR(50),
    channelTitle VARCHAR(100),
    videoTitle TEXT,
    publishedAt DATETIME,
    videoCategoryLabel VARCHAR(100),
    durationSec INT,
    viewCount BIGINT,
    likeCount BIGINT,
    commentCount BIGINT,
    tags TEXT
);

SHOW TABLES;

SELECT COUNT(*) AS youtube_count
FROM youtube_videos;

SELECT COUNT(DISTINCT videoId) AS unique_videos
FROM youtube_videos;

SELECT *
FROM youtube_videos
LIMIT 5;

SELECT COUNT(*) AS match_count
FROM matches;

SELECT *
FROM matches
LIMIT 5;