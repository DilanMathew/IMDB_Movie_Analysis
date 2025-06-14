import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV
@st.cache_data
def load_data():
    return pd.read_csv("imdb_2024_movies_detailed.csv")

df = load_data()

st.title("🎬 IMDb 2024 Movie Insights Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Duration Filter
duration_filter = st.sidebar.selectbox(
    "Select Duration Range (in hours)",
    ("All", "< 2 hrs", "2 - 3 hrs", "> 3 hrs")
)

if duration_filter != "All":
    if duration_filter == "< 2 hrs":
        df = df[df['Duration_Minutes'] < 120]
    elif duration_filter == "2 - 3 hrs":
        df = df[(df['Duration_Minutes'] >= 120) & (df['Duration_Minutes'] <= 180)]
    elif duration_filter == "> 3 hrs":
        df = df[df['Duration_Minutes'] > 180]

# Ratings Filter
min_rating = st.sidebar.slider("Minimum IMDb Rating", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
df = df[df['Rating'] >= min_rating]

# Votes Filter
min_votes = st.sidebar.number_input("Minimum Votes", min_value=0, value=0, step=1000)
df = df[df['Votes'] >= min_votes]

# Genre Filter
selected_genres = st.sidebar.multiselect("Select Genres", df['Genres'].unique())
if selected_genres:
    df = df[df['Genres'].isin(selected_genres)]

# --- Filtered DataFrame View ---
st.subheader("🎯 Filtered Movies Table")
st.dataframe(df[['Title', 'Genres', 'Rating', 'Votes', 'Duration_Minutes']].reset_index(drop=True))

# --- Top 10 Movies by Rating ---
st.subheader("⭐ Top 10 Movies by Rating")
top_rating = df.sort_values(by="Rating", ascending=False).head(10)
st.dataframe(top_rating[['Title', 'Rating', 'Votes']])

# --- Top 10 Movies by Votes ---
st.subheader("📈 Top 10 Movies by Votes")
top_votes = df.sort_values(by="Votes", ascending=False).head(10)
st.dataframe(top_votes[['Title', 'Votes', 'Rating']])

# --- Genre Distribution ---
st.subheader("🎭 Genre Distribution")
genre_counts = df['Genres'].value_counts()
fig1, ax1 = plt.subplots()
sns.barplot(x=genre_counts.values, y=genre_counts.index, ax=ax1)
ax1.set_xlabel("Movie Count")
st.pyplot(fig1)

# --- Average Duration by Genre ---
st.subheader("🕒 Average Duration by Genre")
avg_duration = df.groupby("Genres")["Duration_Minutes"].mean().sort_values()
fig2, ax2 = plt.subplots()
ax2.barh(avg_duration.index, avg_duration.values)
ax2.set_xlabel("Average Duration (min)")
st.pyplot(fig2)

# --- Voting Trends by Genre ---
st.subheader("🗳️ Voting Trends by Genre")
avg_votes = df.groupby("Genres")["Votes"].mean().sort_values(ascending=False)
fig3, ax3 = plt.subplots()
sns.barplot(x=avg_votes.values, y=avg_votes.index, ax=ax3)
ax3.set_xlabel("Average Votes")
st.pyplot(fig3)

# --- Rating Distribution ---
st.subheader("📊 Rating Distribution")
fig4, ax4 = plt.subplots()
sns.histplot(df['Rating'], bins=20, kde=True, ax=ax4)
ax4.set_xlabel("Rating")
st.pyplot(fig4)

# --- Genre-Based Rating Leaders ---
st.subheader("🏆 Top-Rated Movies per Genre")
top_genre_movies = df.loc[df.groupby("Genres")["Rating"].idxmax()]
st.dataframe(top_genre_movies[['Genres', 'Title', 'Rating']].sort_values(by='Rating', ascending=False))

# --- Most Popular Genres by Voting ---
st.subheader("🔥 Most Popular Genres by Total Votes")
total_votes = df.groupby("Genres")["Votes"].sum().sort_values(ascending=False)
fig5, ax5 = plt.subplots()
ax5.pie(total_votes.values, labels=total_votes.index, autopct="%1.1f%%", startangle=90)
ax5.axis("equal")
st.pyplot(fig5)

# --- Duration Extremes ---
st.subheader("🎥 Duration Extremes")
shortest = df[df['Duration_Minutes'] == df['Duration_Minutes'].min()]
longest = df[df['Duration_Minutes'] == df['Duration_Minutes'].max()]
st.write("**Shortest Movie:**")
st.table(shortest[['Title', 'Duration_Minutes']])
st.write("**Longest Movie:**")
st.table(longest[['Title', 'Duration_Minutes']])

# --- Ratings by Genre (Heatmap) ---
st.subheader("🔥 Heatmap of Average Ratings by Genre")
rating_heatmap = df.groupby("Genres")["Rating"].mean().to_frame().T
fig6, ax6 = plt.subplots()
sns.heatmap(rating_heatmap, cmap="coolwarm", annot=True, ax=ax6)
ax6.set_ylabel("Genres")
st.pyplot(fig6)

# --- Correlation Analysis ---
st.subheader("📌 Correlation: Rating vs Votes")
fig7, ax7 = plt.subplots()
sns.scatterplot(data=df, x="Rating", y="Votes", ax=ax7)
ax7.set_title("Rating vs Votes")
st.pyplot(fig7)
