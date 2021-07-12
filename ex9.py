"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very
first exercise)

Extras:

    -Keep the game going until the user types “exit”
    -Keep track of how many guesses the user has taken,
    and when the game ends, print this out.

"""

import random

win = ' Wanna play again? Type a number if yes and "exit" if no: '


def guess(gn, rn):
    if gn > rn:
        return 'too high! '
    elif gn < rn:
        return 'too low! '
    elif gn == rn:
        return win


cmd = input('''In this game you need to guess a number between 1 and 9.
    Your guess? ''')

while cmd != 'exit':
    num = random.randint(1, 9)
    i = 1
    var = True
    while var:
        cmd = int(cmd)
        if guess(cmd, num) == win:
            var = False
            print('exactly right! You have tried {} times.'.format(i))
        cmd = input(guess(cmd, num))
        i = i+1
