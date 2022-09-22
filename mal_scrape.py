# Import libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# Get Content 
page = requests.get("https://myanimelist.net/topanime.php")
soup = bs(page.content, "html.parser") 
results = soup.find(id = "content")

# Extract values
raw_name = results.find_all("img", alt = True)
raw_url = results.find_all("a", class_ = "hoverinfo_trigger fl-l ml12 mr8")
raw_score = results.find_all("td", class_ = "score ac fs14") 
raw_rank = results.find_all("td", class_ = "rank ac")
raw_type = results.find_all("div", class_ = "information di-ib mt4")
raw_episodes = results.find_all("div", class_ = "information di-ib mt4")

list_name = list()
list_url = list()
list_score = list()
list_rank = list()
list_type = list()
list_episodes = list()

for name in raw_name:
    list_name.append(name['alt'].replace("Anime: ", ""))

for url in raw_url:
    list_url.append(url.get('href'))

for score in raw_score:
    list_score.append(score.text)

for rank in raw_rank:
    list_rank.append(rank.text)

for typ in raw_type:
    list_type.append(re.search(r"(TV|OVA|ONA|Movie)", typ.text).group())

for episode in raw_episodes:
    list_episodes.append(re.search(r"(\d*)(?:\seps)", episode.text).group(1))

# Create Dictionary
anime_dict = {'name': list_name, 
              'rank': list_rank, 
              'score': list_score, 
              'type': list_type, 
              'episodes': list_episodes,
              'url': list_url}
