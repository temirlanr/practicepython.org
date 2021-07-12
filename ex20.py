"""
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest
to largest) and another number. The function decides
whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
"""

import random
import time


def random_list(length):
    aa = []
    for i in range(length):
        n = random.randint(1, 1000000)
        aa.append(n)
    return aa


def is_inside(sorted_list, number):
    for num in sorted_list:
        if num == number:
            return True
    return False


def binary_search(sorted_list, number):
    temp = sorted_list
    while True:
        if len(temp) == 2:
            if temp[0] == number or temp[1] == number:
                return True
            break
        elif len(temp) == 1:
            if temp[0] == number:
                return True
            break
        mid = int(len(temp) / 2)
        num = temp[mid]
        if num == number:
            return True
            break
        elif num > number:
            temp = temp[:mid]
        elif num < number:
            temp = temp[mid:]
    return False


if __name__ == "__main__":
    ex = sorted(random_list(100000000))
    #print(ex)
    start_time = time.time()
    print(is_inside(ex, 567))
    #print(binary_search(ex, 567))
    print("--- %s seconds ---" % (time.time() - start_time))

