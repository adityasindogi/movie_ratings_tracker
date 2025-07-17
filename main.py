from scraper import scrape_movies_from_omdb
from analyzer import show_top_movies, show_average_rating, show_movies_by_year, show_director_counts
from visualiser import plot_top_rated_movies, plot_movies_per_year, plot_director_counts, plot_genre_distribution, plot_rating_trend

def main():
    df = scrape_movies_from_omdb()
    if df.empty:
        print("No data to analyze.")
        return

    print(df.to_string(index=False))

    show_top_movies(df)
    show_average_rating(df)
    show_movies_by_year(df)
    show_director_counts(df)

    plot_top_rated_movies(df, n=5)
    plot_movies_per_year(df)
    plot_director_counts(df, n=5)
    plot_genre_distribution(df)
    plot_rating_trend(df)


if __name__ == "__main__":
    main()
