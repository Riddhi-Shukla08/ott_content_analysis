# ott_content_analysis

OTT platforms have a large and diverse content catalogue. This project analyzes an OTT content dataset to identify trends in content type, release years, ratings, countries, genres, and movie duration.  The project uses **Excel, MySQL, and Python** to perform data cleaning, exploratory data analysis, SQL-based analysis, and visualization.
🎯 Objectives

- Analyze the distribution of Movies and TV Shows
- Identify content trends across release years
- Analyze the most common content ratings
- Explore countries represented in the OTT catalogue
- Identify major genre patterns
- Analyze movie duration
- Generate actionable insights for OTT content strategy

---

## 🛠️ Tools & Technologies

- **Microsoft Excel** – Data preparation, PivotTables and charts
- **MySQL** – Database management and SQL analysis
- **Python** – Exploratory Data Analysis
- **Pandas** – Data manipulation
- **Matplotlib** – Visualization
- **Seaborn** – Visualization

---

## 📂 Project Structure

```text
OTT_Content_Trend_Analysis
│
├── Dataset
│   └── netflix_titles.csv
│
├── Excel
│   └── OTT_Content_Analysis.xlsx
│
├── SQL
│   └── OTT_Content_Analysis.sql
│
├── Python
│   └── OTT_Content_Trend_Analysis.ipynb
│
├── Visualizations
│   ├── 01_movies_vs_tv_shows.png
│   ├── 02_content_added_by_year.png
│   ├── 03_top_ratings.png
│   ├── 04_release_year_trend.png
│   ├── 05_top_countries.png
│   ├── 06_movie_duration.png
│   ├── 07_movies_vs_tv_over_time.png
│   └── 08_top_genres.png
│
└── Report
    └── Content_Strategy_Memo.docx
📊 Analysis Performed
Excel Analysis

The dataset was analyzed using Excel PivotTables and charts for:

Movies vs TV Shows
Content distribution by release year
Content ratings
Top countries
Top genre combinations
Movie duration
SQL Analysis

SQL queries were used to perform:

Total content count
Movies vs TV Shows comparison
Year-wise content analysis
Rating analysis
Country-level analysis
Recent content analysis
Movie duration analysis
TV Show season analysis
Missing-value checks
Duplicate checks
Python Analysis

Python was used for:

Data loading
Data cleaning
Missing-value analysis
Duplicate checking
Exploratory Data Analysis
Data visualization

The Python analysis includes 8 visualizations covering content type, content-added trends, ratings, release years, countries, movie duration, content type over time, and genres.

📈 Key Insights

The analysis provides insights into:

The overall balance between Movies and TV Shows.
How the OTT catalogue is distributed across release years.
The most frequently occurring content ratings.
Geographic representation of the catalogue.
Major genre patterns.
Distribution of movie durations.
Changes in Movies and TV Shows across release years.
💡 Content Strategy Recommendations
Maintain a balanced content portfolio across Movies and TV Shows.
Monitor genre and rating trends together to understand audience segments.
Analyze regional content patterns to identify opportunities for localized content.
Track content freshness by comparing release years with content-added years.
Use movie duration along with engagement metrics when planning future content.
📄 Deliverables

The project includes:

Excel analysis workbook
SQL database and queries
Python EDA notebook
Data visualizations
Content Strategy Memo
🔍 Conclusion

This project demonstrates how Excel, SQL, and Python can be combined to analyze OTT content data and convert raw catalogue information into meaningful business insights.

The analysis can be further enhanced by incorporating user-level data such as watch time, completion rate, ratings, and engagement to support more detailed content strategy decisions.
