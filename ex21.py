"""
Take the code from the How To Decode A Website exercise
(if you didn’t do it or just want to play with some
different code, use the code from the solution), and
instead of printing the results to a screen, write
the results to a txt file. In your code, just make up
a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
soup = BeautifulSoup(r.text)
file_name = input("Enter a name for a file: ")

with open('{}.txt'.format(file_name), 'w') as open_file:
    for paragraph in soup.find_all(class_='paywall'):
        if paragraph.p:
            open_file.write(paragraph.p.text.strip() + "\n")
        else:
            temp = paragraph.contents[0]
            open_file.write(temp + "\n")
