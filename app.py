import requests as req
import html
from bs4 import BeautifulSoup

from helpers.read import read_csv_file
from helpers.write import write_csv_file

# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe

def scrape_music():

    # Log that script is started
    print("Beginning to scrape . . .")

    # Get HTML from 90.3 Core FM website
    url = "http://thecore.fm/public/index.php"
    res = req.get(url)
    page_html = res.content

    # Beautiful Soap HTML parser
    soup = BeautifulSoup(page_html, "html.parser")

    # Use HTML parser and response to get recently played songs
    list_of_scraped_music = []
    try:

        # Parse for recently played songs
        recently_played = soup.find("span", attrs={"id": "justplayed"})
        recently_played = recently_played.findChildren()
        recently_played = recently_played[4]
        recently_played = recently_played.find("br")
        recently_played = recently_played.prettify().split("<br>")

        # Split by "-" dash to build list of artist / song dictionaries
        # Collects the latest 4. The more current one (5th) is not getting collected in scrape
        for i in range(1,len(recently_played)):
            artist = recently_played[i].strip().split(" - ")[0].replace("</br>","").strip()
            song = recently_played[i].strip().split(" - ")[1].replace("</br>","").strip()
            list_of_scraped_music.append({"artist": artist, "song": song})

        print("Scrape completed")

    except Exception as e:
        print("Scrape was not successful")


    # test data
    # print(list_of_scraped_music)
    # list_of_scraped_music = [{'artist': 'The Beatles', 'song': 'A Day In The Life'}, {'artist': 'Test Artist 1', 'song': 'Test Song 1'}, {'artist': 'Test Artist 2', 'song': 'Test Song 2'}]
    # list_of_scraped_music = []

    # Only Read to File if scrape was successful
    list_of_new_music = list_of_scraped_music
    if list_of_scraped_music:

        # Read CSV File for existing content
        list_of_existing_music = read_csv_file()

        # Compare scraped music with existing file, remove any existing music from th
        for existing_row in list_of_existing_music:
            for scraped_row in list_of_new_music:
                if (existing_row["artist"] == scraped_row["artist"]) and (existing_row["song"] == scraped_row["song"]):
                    list_of_new_music.remove(scraped_row)

    # Only Write to File if scrape contained unique value
    if list_of_new_music:
        write_csv_file(list_of_new_music)
