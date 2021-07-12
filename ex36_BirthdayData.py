"""
In the previous exercise we counted how many birthdays
there are in each month in our dictionary of birthdays.

In this exercise, use the bokeh Python library to plot
a histogram of which months the scientists have birthdays
in! Because it would take a long time for you to input
the months of various scientists, you can use my scientist
 birthday JSON file. Just parse out the months (if you don’t
 know how, I suggest looking at the previous exercise or its
 solution) and draw your histogram.

If you are using a purely web-based interface for coding,
this exercise won’t work for you, since it requires installing
the bokeh Python package. Now might be a good time to install
Python on your own computer.
"""

from bokeh.plotting import figure, show, output_file
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
        birthdays.append("July")
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

output_file("plot.html")

x_categories = ["January", "February", "March",
                "April", "May", "June", "July",
                "August", "September", "October",
                "November", "December"]
x = list(c.keys())
y = []
for item in x:
    y.append(c[item])

p = figure(x_range=x_categories, plot_width=1000)
p.vbar(x=x, top=y, width=0.5)

show(p)
