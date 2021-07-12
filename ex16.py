"""
Write a password generator in Python.
Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating
a new password every time the user asks for
a new password. Include your run-time code
in a main method.

Extra:

Ask the user how strong they want their
password to be. For weak passwords, pick
a word or two from a list.
"""

import random
import time


def password_generator(text="Generating password..."):
    print(text)
    res = []
    for i in range(16):
        res.append(random.choice('_.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    return ''.join(res)


start_time = time.time()
print(password_generator())
print("--- %s seconds ---" % (time.time() - start_time))
