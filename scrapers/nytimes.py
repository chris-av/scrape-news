import requests
import re
from bs4 import BeautifulSoup, Tag
from utils.colors import Colors

class NYTimes:
    def __init__(self) -> None:
        self.homepage_url = "https://nytimes.com"
        self.session = requests.session()
        self.colors = Colors()
        pass

    def get_homepage(self):

        print("")
        print(f"{self.colors.GREEN}#######################################{self.colors.RESET}")
        print(f"{self.colors.GREEN}#############             #############{self.colors.RESET}")
        print(f"{self.colors.GREEN}#############   NYTIMES   #############{self.colors.RESET}")
        print(f"{self.colors.GREEN}#############             #############{self.colors.RESET}")
        print(f"{self.colors.GREEN}#######################################{self.colors.RESET}")

        response = self.session.get(self.homepage_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        main_soup = soup.find("main")

        if not isinstance(main_soup, Tag):
            raise Exception("main_soup not of type Tag")

        main_content = main_soup.find("div", { "class": re.compile(r"desktop", re.I) })

        if not isinstance(main_content, Tag):
            raise Exception("main_content not of type tag")

        live_feed_soup = main_content.find("section", { "id": "hp-live-band-container" })

        if not isinstance(live_feed_soup, Tag):
            raise Exception("main_content not of type tag")
        
        print("")
        print(f"{self.colors.BOLD}{self.colors.RED}## LIVE UPDATES{self.colors.RESET}")
        print("")

        for stories in live_feed_soup.find_all("a"):
            txt = stories.find("p").get_text()
            time = stories.find("span").get_text()
            if txt.lower() == "live":
                continue
            print("  ", end="")
            print(f"{txt} - {time}")
        print("")

        stories_sections = main_content.find_all("div", { "data-hierarchy": "zone" })
        if len(stories_sections) < 2:
            raise Exception("did not find stories")

        stories_section = stories_sections[1]

        print("")
        print(f"{self.colors.BOLD}{self.colors.RED}## DEVELOPING STORIES{self.colors.RESET}")
        print("")

        stories = stories_section.find_all("p", { "class": re.compile(r"indicate-hover", re.I) })
        for story in stories:
            print("  ", end="")
            txt = story.get_text()
            print(f"{txt}")

        print("")

        print("")
        print(f"{self.colors.BOLD}{self.colors.RED}## OPINION{self.colors.RESET}")
        print("")

        opinion_section = stories_sections[2]
        for opinion in opinion_section.find_all("a"):
            parag = opinion.find_all("p")
            if len(parag) == 0:
                continue
            print("  ", end="")
            author = parag[0].get_text()
            title = parag[1].get_text()
            print(f"{title} - {self.colors.GREEN}{author}{self.colors.RESET}")

        print("")
        return
