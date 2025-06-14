# 🎬 IMDB 2024 Data Scraping and Visualization

## 🚀 Project Overview

This project focuses on **extracting and analyzing IMDb's 2024 movie data** using web scraping, data cleaning, SQL storage, and interactive visualizations in Streamlit.

### 🎯 Goal:
- Scrape IMDb movie data (2024)
- Analyze key trends in genres, ratings, votes, durations
- Store structured data in MySQL
- Provide a fully interactive Streamlit dashboard for users

---

## 🧠 Skills Used

- 🐍 Python
- 🧹 Data Cleaning (Pandas)
- 🕸️ Web Scraping (Selenium)
- 📊 Data Analysis & Visualization (Matplotlib, Seaborn)
- 🗄️ SQL (MySQL)
- 🧮 Interactive Dashboards (Streamlit)

---

## 🏢 Domain
**Entertainment / Data Analytics**

---

## 📌 Problem Statement

Scrape movie data from IMDb's 2024 listings including:
- Movie Titles
- Genres
- Ratings
- Voting Counts
- Duration

After processing, analyze the data and provide genre-based CSVs, an SQL-stored dataset, and a Streamlit web app for filtering and visual analysis.

---

## 💼 Business Use Cases

- 🔝 **Top-Rated Movies**: Identify top 10 highest-rated movies with significant votes.
- 🎭 **Genre Analysis**: Explore movie counts by genre.
- ⏱️ **Duration Insights**: Analyze average movie duration per genre.
- 🗳️ **Voting Patterns**: Discover genres with highest average votes.
- 📈 **Rating Distribution**: Visualize overall IMDb rating spread.
- 🥇 **Top in Genre**: Find highest-rated movie per genre.
- 🍿 **Popular Genres**: Identify most common genres on IMDb.
- 🎥 **Duration Extremes**: Identify shortest and longest 2024 movies.
- 🔥 **Genre vs. Rating Heatmap**
- 📉 **Rating–Votes Correlation**

---

## 🔎 Approach

### 1. 🕷️ Data Scraping
- ✅ Source: IMDb 2024 Movies Page
- ✅ Tool: Selenium
- ✅ Fields: Title, Genre, Ratings, Votes, Duration
- ✅ Saved as: Individual CSVs per genre + Combined CSV

### 2. 🧼 Data Cleaning & Storage
- ✅ Handled missing values (`N/A`, empty strings)
- ✅ Converted data types (votes to `int`, ratings to `float`)
- ✅ Final data stored in MySQL (using SQL scripts or Workbench import)

### 3. 📊 Streamlit Visualizations

Interactive plots and filters included:
- 📌 Top 10 Movies (Rating & Votes)
- 📊 Genre Distribution
- 📏 Average Duration by Genre
- 🗳️ Voting Trends by Genre
- 📈 Rating Distribution (Histogram/Boxplot)
- 🥇 Genre-Based Rating Leaders (Table)
- 🧮 Most Voted Genres (Pie chart)
- 🕐 Duration Extremes (Cards or Table)
- 🔥 Ratings Heatmap (Genre vs. Rating)
- 🔗 Votes vs. Ratings Correlation (Scatter)

---

## 🎛️ Interactive Filters (Streamlit)
Users can filter movies based on:
- 📏 Duration (e.g. < 2 hrs, 2–3 hrs, > 3 hrs)
- ⭐ IMDb Rating (e.g. > 8.0)
- 🗳️ Votes (e.g. > 10,000)
- 🎭 Genre (Action, Drama, etc.)

Filtered movies are dynamically displayed in a table.

---

## 🧾 Dataset Format

| Column         | Description                        |
|----------------|------------------------------------|
| Title          | Movie title with order index       |
| Link           | IMDb link to the movie             |
| Genres         | Comma-separated genre(s)           |
| Directors      | Director name                      |
| Rating         | IMDb rating                        |
| Votes          | Total IMDb votes                   |
| Duration       | Movie runtime (e.g. 1 hr 51 min)   |

---

## 🛠️ Tech Stack

| Component     | Tools Used                                      |
|---------------|-------------------------------------------------|
| Language      | Python                                          |
| Database      | MySQL                                           |
| Visualization | Matplotlib, Seaborn, Streamlit                  |
| Libraries     | Selenium, Pandas, SQLAlchemy, Streamlit         |

---

## 📦 Project Structure

