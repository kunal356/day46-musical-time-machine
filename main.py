import requests
from bs4 import BeautifulSoup
import spotipy
from config import APP_CLIENT_ID, APP_SECRET
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD")
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
top_100 = [i.text.strip() for i in soup.select("li.o-chart-results-list__item h3.c-title")]
playlist = []
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8080",
        client_id=APP_CLIENT_ID,
        client_secret=APP_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="kunal",
    )
)
user_id = sp.current_user()["id"]
year = date.split("-")[0]
for song in top_100:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        playlist.append(result["tracks"]["items"][0]["uri"])
        print(f"{song} added")
    except IndexError:
        print(f"{song} passed")
        pass
print(len(playlist))
print(playlist)
playlist_resp = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_id = playlist_resp['id']
print(playlist_id)
sp.playlist_add_items(playlist_id=playlist_id, items=playlist)
