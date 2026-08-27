USE premier_league_media;

SELECT Season,COUNT(*) AS total_matches
FROM matches
GROUP BY Season
ORDER BY Season;

SELECT Season,FTR AS result, COUNT(*) AS matches
FROM matches
GROUP BY Season, FTR
ORDER BY Season, FTR;

SELECT Season,
    SUM(CASE WHEN FTR = 'H' THEN 1 ELSE 0 END) AS HomeWins,
    SUM(CASE WHEN FTR = 'D' THEN 1 ELSE 0 END) AS Draws,
    SUM(CASE WHEN FTR = 'A' THEN 1 ELSE 0 END) AS AwayWins
FROM matches
GROUP BY Season
ORDER BY Season;

SELECT Season,
    ROUND(AVG(FTHG + FTAG), 2) AS AvgGoalsPerMatch
FROM matches
GROUP BY Season
ORDER BY Season;

