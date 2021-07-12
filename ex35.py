"""
In the previous exercise we saved information about
famous scientists’ names and birthdays to disk. In
this exercise, load that JSON file from disk, extract
the months of all the birthdays, and count how many
scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""

from collections import Counter
import json

with open("info.json", "r") as read_file:
    info = json.load(read_file)

keys = info.keys()
birthdays = []
for key in keys:
    birthday = info[key]
    if birthday[1] == 1:
        birthdays.append("January")
    elif birthday[1] == 2:
        birthdays.append("February")
    elif birthday[1] == 3:
        birthdays.append("March")
    elif birthday[1] == 4:
        birthdays.append("April")
    elif birthday[1] == 5:
        birthdays.append("May")
    elif birthday[1] == 6:
        birthdays.append("June")
    elif birthday[1] == 7:
        birthdays.append("Jule")
    elif birthday[1] == 8:
        birthdays.append("August")
    elif birthday[1] == 9:
        birthdays.append("September")
    elif birthday[1] == 10:
        birthdays.append("October")
    elif birthday[1] == 11:
        birthdays.append("November")
    elif birthday[1] == 12:
        birthdays.append("December")

c = Counter(birthdays)
print(c)
