"""
Using the requests and BeautifulSoup Python libraries,
print to the screen the full text of the article on this
website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages.
Your task is to print out the text to the screen so that
you can read the full article without having to click any
buttons.

This will just print the full text of the article to the screen.
It will not make it easy to read, so next exercise we will
learn how to write this text to a .txt file.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup = BeautifulSoup(r.text)

#p1 = soup.find(class_="has-dropcap")
#p2 = soup.find("It was early 2001")
#print(p1.p.text)
#print(p2.p.text)

for paragraph in soup.find_all(class_='paywall'):
    if paragraph.p:
        print(paragraph.p.text.strip())
    else:
        print(paragraph.contents[0])

