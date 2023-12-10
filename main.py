import requests
import sys
from bs4 import BeautifulSoup
from utils.formatter import format_title, format_paragraph


args = sys.argv
if len(args) < 2:
    print("did not supply enough arguments")
    raise Exception("did not supply enough arguments, please pass a full link")


link = args[1]
if len(args) > 2:
    print(f"passed in multiple args, assuming that the link is {link}")
    print("")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
}

response = requests.get(link, headers=headers)

if response.status_code != 200:
    raise Exception("status code is not 200, throwing error")



soup = BeautifulSoup(response.content, "lxml")
title = soup.find("h1")
paragraphs = soup.findAll("p")


if title:
    print(format_title(title.text))
else:
    print("could not find title ... ")
    print("")

print("")
print("")


for paragraph in paragraphs:
    print(format_paragraph(paragraph.text))
    print("")

