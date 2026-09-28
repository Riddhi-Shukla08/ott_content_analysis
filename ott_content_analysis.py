# ============================================
# OTT CONTENT TREND ANALYSIS
# ============================================

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 2. Load Excel File
df = pd.read_excel("OTT_Content_Analysis.xlsx")

print("Excel file loaded successfully!")
print(df.head())


# ============================================
# 3. BASIC DATA UNDERSTANDING
# ============================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


# ============================================
# 4. MISSING VALUES
# ============================================

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================
# 5. DUPLICATE ROWS
# ============================================

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# ============================================
# 6. DATA CLEANING
# ============================================

# Convert date_added into date format
df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)

# Extract year when content was added
df['added_year'] = df['date_added'].dt.year


# ============================================
# 7. MOVIES VS TV SHOWS
# ============================================

plt.figure(figsize=(7,5))

sns.countplot(
    data=df,
    x='type'
)

plt.title('Movies vs TV Shows')
plt.xlabel('Content Type')
plt.ylabel('Number of Titles')

plt.tight_layout()
plt.show()


# ============================================
# 8. CONTENT ADDED BY YEAR
# ============================================

content_added = (
    df['added_year']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(10,5))

plt.plot(
    content_added.index,
    content_added.values,
    marker='o'
)

plt.title('Content Added by Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================
# 9. TOP 10 CONTENT RATINGS
# ============================================

top_ratings = (
    df['rating']
    .dropna()
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top_ratings.values,
    y=top_ratings.index
)

plt.title('Top 10 Content Ratings')
plt.xlabel('Number of Titles')
plt.ylabel('Rating')

plt.tight_layout()
plt.show()


# ============================================
# 10. RELEASE YEAR TREND
# ============================================

release_trend = (
    df['release_year']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12,5))

plt.plot(
    release_trend.index,
    release_trend.values
)

plt.title('Content Distribution by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')

plt.tight_layout()
plt.show()


# ============================================
# 11. TOP 10 COUNTRIES
# ============================================

df['primary_country'] = (
    df['country']
    .fillna('Unknown')
    .str.split(',')
    .str[0]
    .str.strip()
)

top_countries = (
    df['primary_country']
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title('Top 10 Countries by Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')

plt.tight_layout()
plt.show()


# ============================================
# 12. MOVIE DURATION DISTRIBUTION
# ============================================

# Make sure duration is numeric
df['Movie Duration (Minutes)'] = pd.to_numeric(
    df['Movie Duration (Minutes)'],
    errors='coerce'
)

plt.figure(figsize=(10,5))

sns.histplot(
    df['Movie Duration (Minutes)'].dropna(),
    bins=30
)

plt.title('Movie Duration Distribution')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')

plt.tight_layout()
plt.show()


# ============================================
# 13. MOVIES VS TV SHOWS OVER RELEASE YEARS
# ============================================

type_year = (
    df.groupby(['release_year', 'type'])
    .size()
    .unstack(fill_value=0)
)

plt.figure(figsize=(12,6))

if 'Movie' in type_year.columns:
    plt.plot(
        type_year.index,
        type_year['Movie'],
        label='Movies'
    )

if 'TV Show' in type_year.columns:
    plt.plot(
        type_year.index,
        type_year['TV Show'],
        label='TV Shows'
    )

plt.title('Movies vs TV Shows Across Release Years')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')

plt.legend()

plt.tight_layout()
plt.show()


# ============================================
# 14. TOP 10 GENRES
# ============================================

df['primary_genre'] = (
    df['listed_in']
    .fillna('Unknown')
    .str.split(',')
    .str[0]
    .str.strip()
)

top_genres = (
    df['primary_genre']
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,6))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title('Top 10 Genres')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')

plt.tight_layout()
plt.show()


# ============================================
# 15. FINAL SUMMARY
# ============================================

print("\n================================")
print("OTT CONTENT ANALYSIS SUMMARY")
print("================================")

print("\nTotal Titles:")
print(len(df))

print("\nContent Type:")
print(df['type'].value_counts())

print("\nTop 5 Ratings:")
print(df['rating'].value_counts().head(5))

print("\nTop 5 Countries:")
print(df['primary_country'].value_counts().head(5))

print("\nTop 5 Genres:")
print(df['primary_genre'].value_counts().head(5))

print("\nAverage Movie Duration:")
print(
    round(
        df['Movie Duration (Minutes)'].mean(),
        2
    )
)
