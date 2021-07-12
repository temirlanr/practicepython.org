"""
Write a program (using functions!) that asks
the user for a long string containing multiple
words. Print back to the user the same string,
except with the words in backwards order.
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""


def backwards(text="Enter some text with multiple words: "):
    temp = input(text)
    temp = temp.split()
    return ' '.join(temp[::-1])


print(backwards())
