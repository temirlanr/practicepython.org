"""
In the previous exercise we created a dictionary of famous
scientists’ birthdays. In this exercise, modify your program
from Part 1 to load the birthday dictionary from a JSON file
on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday
to add to the dictionary, and update the JSON file you have
on disk with the scientist’s name. If you run the program
 multiple times and keep adding new names, your JSON file
 should keep getting bigger and bigger.
"""

import json

with open("info.json", "r") as read_file:
    info = json.load(read_file)

keys = info.keys()
for key in keys:
    print("{}".format(key))

new_name = input("Enter a name to add: ")
new_birthday = [int(x) for x in input("Enter Day Month Year separated by space bar: ").split()]
info[new_name] = new_birthday

with open("info.json", "w") as overwrite:
    json.dump(info, overwrite)
