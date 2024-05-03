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
print(top_100)

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
print(user_id)

