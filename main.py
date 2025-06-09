from scrapers.nytimes import NYTimes

def main():
    scraper = NYTimes()
    scraper.get_homepage()

if __name__ == "__main__":
    main()
