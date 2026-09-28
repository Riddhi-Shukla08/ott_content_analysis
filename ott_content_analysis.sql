CREATE DATABASE ott_content_analysis;

USE ott_content_analysis;

CREATE TABLE ott_titles (
    show_id VARCHAR(20),
    type VARCHAR(20),
    title VARCHAR(255),
    director TEXT,
    cast TEXT,
    country TEXT,
    date_added VARCHAR(50),
    release_year INT,
    rating VARCHAR(30),
    duration VARCHAR(30),
    listed_in TEXT,
    description TEXT
);

DESCRIBE ott_titles;

SELECT COUNT(*) AS total_titles
FROM ott_titles;

SELECT
    type,
    COUNT(*) AS total_titles
FROM ott_titles
GROUP BY type
ORDER BY total_titles DESC;

SELECT
    release_year,
    COUNT(*) AS total_titles
FROM ott_titles
GROUP BY release_year
ORDER BY release_year;

SELECT
    rating,
    COUNT(*) AS total_titles
FROM ott_titles
WHERE rating IS NOT NULL
GROUP BY rating
ORDER BY total_titles DESC;

SELECT
    country,
    COUNT(*) AS total_titles
FROM ott_titles
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_titles DESC
LIMIT 15;

SELECT
    release_year,
    COUNT(*) AS total_titles
FROM ott_titles
WHERE release_year >= 2015
GROUP BY release_year
ORDER BY release_year DESC;

SELECT
    release_year,
    type,
    COUNT(*) AS total_titles
    FROM ott_titles
GROUP BY release_year, type
ORDER BY release_year, type;

SELECT
    type,
    rating,
    COUNT(*) AS total_titles
FROM ott_titles
WHERE rating IS NOT NULL
GROUP BY type, rating
ORDER BY type, total_titles DESC;

SELECT
    title,
    type,
    release_year,
    rating,
    duration
FROM ott_titles
WHERE release_year >= 2020
ORDER BY release_year DESC;

SELECT
    title,
    duration,
    release_year,
    rating
FROM ott_titles
WHERE type = 'Movie'
AND duration LIKE '% min'
ORDER BY
    CAST(REPLACE(duration, ' min', '') AS UNSIGNED) DESC
LIMIT 20;

SELECT
    title,
    duration,
    release_year,
    rating
FROM ott_titles
WHERE type = 'Movie'
AND duration LIKE '% min'
ORDER BY
    CAST(REPLACE(duration, ' min', '') AS UNSIGNED)
LIMIT 20;

SELECT
    title,
    duration,
    release_year,
    rating
FROM ott_titles
WHERE type = 'TV Show'
ORDER BY
    CAST(REPLACE(duration, ' Seasons', '') AS UNSIGNED) DESC
LIMIT 20;

SELECT
    release_year,
    SUM(CASE WHEN type = 'Movie' THEN 1 ELSE 0 END) AS movies,
    SUM(CASE WHEN type = 'TV Show' THEN 1 ELSE 0 END) AS tv_shows
FROM ott_titles
GROUP BY release_year
ORDER BY release_year;

SELECT
    SUM(CASE WHEN director IS NULL OR director = '' THEN 1 ELSE 0 END) AS missing_director,
    SUM(CASE WHEN cast IS NULL OR cast = '' THEN 1 ELSE 0 END) AS missing_cast,
    SUM(CASE WHEN country IS NULL OR country = '' THEN 1 ELSE 0 END) AS missing_country,
    SUM(CASE WHEN rating IS NULL OR rating = '' THEN 1 ELSE 0 END) AS missing_rating
FROM ott_titles;

SELECT
    show_id,
    COUNT(*) AS duplicate_count
FROM ott_titles
GROUP BY show_id
HAVING COUNT(*) > 1;

SELECT
    title,
    type,
    release_year,
    rating,
    duration
FROM ott_titles
ORDER BY release_year DESC
LIMIT 20;

SELECT
    COUNT(*) AS total_titles,
    COUNT(DISTINCT title) AS unique_titles,
    MIN(release_year) AS earliest_release_year,
    MAX(release_year) AS latest_release_year
FROM ott_titles;
