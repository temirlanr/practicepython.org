"""
For this exercise, we will keep track of when our friend’s
birthdays are, and be able to find that information based on
their name. Create a dictionary (in your file) of names and
birthdays. When you run your program it should ask the user
to enter a name, and return the birthday of that person back
to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!
"""


def get_birthday(dict):
    person = input("Who's birthday do you want to look up? \n")
    birthday = dict[person]
    return "{}/{}/{}".format(*birthday)


friends = {
    "First": [1, 6, 1991],
    "Second": [2, 9, 2001],
    "Third": [3, 12, 1997]
}

print(
    "Welcome to the birthday dictionary. We know the birthdays of: "
)
keys = friends.keys()
for key in keys:
    print("{}".format(key))

print(get_birthday(friends))
