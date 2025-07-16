def show_top_movies(df, n=5):
    print(f"\n🎬 Top {n} Movies by IMDb Rating:")
    top = df.sort_values(by="Rating", ascending=False).head(n)
    print(top[["Title", "Year", "Rating"]].to_string(index=False))

def show_average_rating(df):
    avg = df["Rating"].mean()
    print(f"\n📊 Average IMDb Rating: {avg:.2f}")

def show_movies_by_year(df):
    print("\n📅 Movies Grouped by Release Year:")
    print(df["Year"].value_counts().sort_index())

def show_director_counts(df):
    print("\n🎬 Number of Movies per Director:")
    print(df["Director"].value_counts())
