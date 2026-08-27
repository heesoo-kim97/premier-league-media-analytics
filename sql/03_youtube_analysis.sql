USE premier_league_media;

SELECT YEAR(publishedAt) AS Year,
    COUNT(*) AS TotalVideos,
    ROUND(AVG(viewCount), 0) AS AvgViews
FROM youtube_videos
GROUP BY YEAR(publishedAt)
ORDER BY Year;

SELECT videoTitle, publishedAt, viewCount
FROM youtube_videos
ORDER BY viewCount DESC
LIMIT 10;

SELECT videoCategoryLabel AS Category,
    COUNT(*) AS TotalVideos,
    ROUND(AVG(viewCount), 0) AS AvgViews
FROM youtube_videos
GROUP BY videoCategoryLabel
ORDER BY AvgViews DESC;

SELECT
    CASE
        WHEN durationSec < 60 THEN 'Under 1 min'
        WHEN durationSec < 300 THEN '1–5 min'
        WHEN durationSec < 600 THEN '5–10 min'
        ELSE '10+ min'
    END AS VideoLength,
    COUNT(*) AS TotalVideos,
    ROUND(AVG(viewCount), 0) AS AvgViews
FROM youtube_videos
GROUP BY VideoLength
ORDER BY AvgViews DESC;

