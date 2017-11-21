import requests as req
import html
from bs4 import BeautifulSoup

import csv

# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

# Get HTML from 90.3 Core FM website
url = "http://thecore.fm/public/index.php"
res = req.get(url)
page_html = res.content

# Beautiful Soap HTML parser
soup = BeautifulSoup(page_html, "html.parser")

# Parse for recently played songs
recently_played = soup.find("span", attrs={"id": "justplayed"})
recently_played = recently_played.findChildren()
recently_played = recently_played[4]
recently_played = recently_played.find("br")
recently_played = recently_played.prettify().split("<br>")

# Split by "-" dash to build list of artist / song dictionaries
list_of_music = []

# Only taking middle 3 songs (need to re-visit the parsing to get all 5)
for i in range(1,4):
    artist = recently_played[i].strip().split(" - ")[0]
    song = recently_played[i].strip().split(" - ")[1]
    list_of_music.append([artist,song])


myFile = open('artist_song.csv', 'a')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(list_of_music)

#print(list_of_music)
myFile.close()
