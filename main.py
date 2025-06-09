import requests
import sys
from bs4 import BeautifulSoup
from utils.formatter import format_title, format_paragraph
from utils.parse_args import extract_args


args = sys.argv[1:]
if len(args) < 1:
    print("did not supply enough arguments")
    raise Exception("did not supply enough arguments, please pass a full link")


config = extract_args(args)
link = config["link"]
headers = config["headers"]
max_w = config["max-w"]
padding = config["padding"]
session = requests.session()
session.cookies.clear()
response = session.get(link, headers=headers)
response.raise_for_status()


soup = BeautifulSoup(response.content, "lxml")
title = soup.find("h1")
paragraphs = soup.findAll("p")


if title:
    print("")
    out = format_title(title.text, max_w=max_w, padding=padding)
    print(out)
else:
    print("could not find title ... ")
    print("")

print("")
print("")


for paragraph in paragraphs:
    out = format_paragraph(paragraph.text, max_w=max_w, padding=padding)
    print(out)
    print("")

