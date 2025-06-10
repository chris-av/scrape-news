from scrapers.nytimes import NYTimes
from scrapers.washingtonpost import WashingtonPost

def main():
    for Scraper in [NYTimes, WashingtonPost]:
        scraper = Scraper()
        scraper.get_homepage()
        print("")
        print("")
        print("")
        print("")

if __name__ == "__main__":
    main()
