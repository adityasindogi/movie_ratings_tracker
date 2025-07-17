import requests
import pandas as pd

API_KEY = "7bca4432"
BASE_URL = "http://www.omdbapi.com/"

MOVIES = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Inception",
    "Fight Club",
    "Forrest Gump",
    "Pulp Fiction",
    "The Matrix",
    "Interstellar",
    "Gladiator"
]

def fetch_movie_data(title):
    params = {
        "apikey": API_KEY,
        "t": title
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return {
                "Title": data.get("Title"),
                "Year": int(data.get("Year", 0)),
                "Rating": float(data.get("imdbRating", 0)),
                "Genre": data.get("Genre"),
                "Director": data.get("Director")
            }
    return None

def scrape_movies_from_omdb():
    movie_data = []
    for title in MOVIES:
        print(f"Fetching: {title}")
        data = fetch_movie_data(title)
        if data:
            movie_data.append(data)
    return pd.DataFrame(movie_data)
