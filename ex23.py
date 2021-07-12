"""
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has
a list of all prime numbers under 1000, and the other .txt
file has a list of happy numbers up to 1000.
"""

temp = []
a = []
b = []

with open('primenumbers.txt') as p:
    line = p.readline()
    while line:
        line = int(line.strip())
        a.append(line)
        line = p.readline()

with open('happynumbers.txt') as h:
    line = h.readline()
    while line:
        line = int(line.strip())
        b.append(line)
        line = h.readline()

for num in b:
    if num in a:
        if num not in temp:
            temp.append(num)

print(temp)
