from curses import beep
from bs4 import BeautifulSoup
import requests

# date = input(
#     "Which year do you wan to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2020-03-01"

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# print(response.ok)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select(
    "li h3", id='title-of-a-story')
song_names = [song.getText().strip('\n\n\t\n\t\n\t\t\n\t\t\t\t\t\t')
              for song in song_names_spans]
print(song_names)
