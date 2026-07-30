import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Netflix Data Visualization", layout="wide")

# Load Dataset
df = pd.read_csv("dataset/netflix_titles.csv")

# Sidebar Filter
st.sidebar.title("Filters")

selected_type = st.sidebar.selectbox(
    "Select Type",
    ["All", "Movie", "TV Show"]
)

# Apply Filter
if selected_type == "All":
    filtered_df = df
else:
    filtered_df = df[df["type"] == selected_type]

# Dashboard Title
st.title("🎬 Netflix Data Visualization Dashboard")
st.write("Created by Sai Rishi Sambaraju")

# Dashboard Metrics
total_titles = len(filtered_df)
total_movies = (filtered_df["type"] == "Movie").sum()
total_tv_shows = (filtered_df["type"] == "TV Show").sum()

total_countries = (
    filtered_df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .nunique()
)

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric("Total Titles", total_titles)
metric2.metric("Movies", total_movies)
metric3.metric("TV Shows", total_tv_shows)
metric4.metric("Countries", total_countries)

st.markdown("---")

# Two Charts Side by Side
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎬 Movies vs TV Shows")
    type_counts = filtered_df["type"].value_counts()
    st.bar_chart(type_counts)

with col2:
    st.subheader("🌍 Top 10 Countries")
    country_counts = (
        filtered_df["country"]
        .dropna()
        .str.split(", ")
        .explode()
        .value_counts()
        .head(10)
    )
    st.bar_chart(country_counts)

st.markdown("---")

# Ratings Chart
st.subheader("⭐ Ratings Distribution")

rating_counts = filtered_df["rating"].value_counts()

st.bar_chart(rating_counts)