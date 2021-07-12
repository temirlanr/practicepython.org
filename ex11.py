"""
Ask the user for a number and determine whether the
number is prime or not. (For those who have forgotten,
a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4
to help you. Take this opportunity to practice using
functions, described below.
"""


def prime(inp="Give me a number: "):
    num = int(input(inp))
    arr = []
    for i in range(2, int(num / 2) + 1):
        if num / i == int(num / i):
            arr.append(i)
    if not arr:
        return "Prime"
    return "Not prime"


print(prime())
