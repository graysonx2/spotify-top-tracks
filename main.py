import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Use them in your script
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-top-read"
))


def show_top_items(time_range='medium_term', limit=10):
    print(f"\n=== Your Top {limit} Tracks ({time_range}) ===")
    top_tracks = sp.current_user_top_tracks(time_range=time_range, limit=limit)
    for idx, item in enumerate(top_tracks['items'], 1):
        print(f"{idx}. {item['name']} by {', '.join([a['name'] for a in item['artists']])}")

    print(f"\n=== Your Top {limit} Artists ({time_range}) ===")
    top_artists = sp.current_user_top_artists(time_range=time_range, limit=limit)
    for idx, artist in enumerate(top_artists['items'], 1):
        print(f"{idx}. {artist['name']}")

# Options: 'short_term' (4 weeks), 'medium_term' (6 months), 'long_term' (years)
show_top_items(time_range='short_term', limit=10)
