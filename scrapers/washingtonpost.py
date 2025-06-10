import requests
import re
from bs4 import BeautifulSoup, Tag
from utils.colors import Colors
from utils.headers import get_random_user_agent

class WashingtonPost:
    def __init__(self) -> None:
        self.homepage_url = "https://washingtonpost.com"
        self.session = requests.sessions.session()

        self.session.headers.update({ "User-Agent": get_random_user_agent() })
        self.session.headers.update({ "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" })
        self.session.headers.update({ "Accept-Language": "en-US,en;q=0.5" })
        self.session.headers.update({ "Accept-Encoding": "gzip, deflate, br, zstd" })
        self.session.headers.update({ "Referer": "https://www.washingtonpost.com/" })
        self.session.headers.update({ "Sec-GPC": "1" })
        self.session.headers.update({"Connection": "keep-alive" })
        self.session.headers.update({ "Upgrade-Insecure-Requests": "1" })
        self.session.headers.update({ "Sec-Fetch-Dest": "document" })
        self.session.headers.update({ "Sec-Fetch-Mode": "navigate" })
        self.session.headers.update({ "Sec-Fetch-Site": "same-origin" })
        self.session.headers.update({ "Priority": "u=0, i" })
        self.session.headers.update({ "TE": "trailers" })


        self.colors = Colors()
        pass

    def get_homepage(self):

        print("")
        print(f"{self.colors.GREEN}#######################################{self.colors.RESET}")
        print(f"{self.colors.GREEN}#########                     #########{self.colors.RESET}")
        print(f"{self.colors.GREEN}#########   WASHINGTON POST   #########{self.colors.RESET}")
        print(f"{self.colors.GREEN}#########                     #########{self.colors.RESET}")
        print(f"{self.colors.GREEN}#######################################{self.colors.RESET}")

        response = self.session.get(self.homepage_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        breaking_section = soup.find("div", { "data-link-group": "alert" })

        if breaking_section is not None and isinstance(breaking_section, Tag):
            print(f"{self.colors.RED}{self.colors.BOLD}## BREAKING{self.colors.RESET}")
            print("")
            links = breaking_section.find_all("a")
            for link in links:
                print("  ", end="")
                print(f"{self.colors.RED} {link.get_text()}{self.colors.RESET}")


        live_updates = soup.find("ul", { "data-link-group": "live-bar" })

        if live_updates:

            print("")
            print(f"{self.colors.BOLD}{self.colors.RED}## LIVE UPDATES{self.colors.RESET}")
            print("")

            for update in live_updates.find_all("a"):
                print("  ", end="")
                print(update.get_text().strip())
            print("")


        headlines = soup.find_all("div", { "data-feature-id": re.compile(r"homepage/story") })

        print("")
        print(f"{self.colors.BOLD}{self.colors.RED}## DEVELOPING STORIES{self.colors.RESET}")
        print("")

        for headline in headlines:
            print("  ", end="")
            txt = headline.find("h2")
            if txt is None:
                continue
            print(txt.get_text())


