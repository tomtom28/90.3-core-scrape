import schedule
import time

# Fire off scraping app every 5 minutes
from app import scrape_music
schedule.every(5).minutes.do(scrape_music)
print "Scraped Scheduled . . ."

while True:
    schedule.run_pending()
    time.sleep(1)
