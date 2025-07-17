import matplotlib.pyplot as plt


def plot_top_rated_movies(df, n=5):
    top_movies = df.sort_values(by="Rating", ascending=False).head(n)

    plt.figure(figsize=(10, 6))
    plt.barh(top_movies["Title"], top_movies["Rating"], color="skyblue")
    plt.xlabel("IMDb Rating")
    plt.title(f"Top {n} Rated Movies")
    plt.gca().invert_yaxis()  # highest rating at top
    plt.tight_layout()
    plt.show()


def plot_movies_per_year(df):
    counts = df["Year"].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    counts.plot(kind="bar", color="lightcoral")
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.title("Movies by Release Year")
    plt.tight_layout()
    plt.show()


def plot_director_counts(df, n=5):
    top_directors = df["Director"].value_counts().head(n)

    plt.figure(figsize=(10, 6))
    top_directors.plot(kind="bar", color="mediumseagreen")
    plt.xlabel("Director")
    plt.ylabel("Number of Movies")
    plt.title(f"Top {n} Directors by Movie Count")

def plot_genre_distribution(df):
    from collections import Counter
    all_genres = []
    for genres in df["Genre"].dropna():
        for g in genres.split(","):
            all_genres.append(g.strip())

    genre_counts = Counter(all_genres)
    top_genres = dict(genre_counts.most_common(6))  # Top 6 genres

    plt.figure(figsize=(8, 8))
    plt.pie(list(top_genres.values()), labels=list(top_genres.keys()), autopct='%1.1f%%', startangle=140)

    plt.title("Top Movie Genres")
    plt.tight_layout()
    plt.savefig("assets/genres_pie.png")  # Save chart to assets folder

    plt.show()

def plot_rating_trend(df):
    yearly_avg = df.groupby("Year")["Rating"].mean().sort_index()

    plt.figure(figsize=(10, 5))
    plt.plot(yearly_avg.index, yearly_avg.values, marker="o", color="darkblue")
    plt.title("Average IMDb Rating by Year")
    plt.xlabel("Year")
    plt.ylabel("Average Rating")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("assets/top5_ratings.png")  # Save chart to assets folder
    plt.show()
