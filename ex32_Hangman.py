"""
In this exercise, we will finish building Hangman.
In the game of Hangman, the player only has 6 incorrect
guesses (head, body, 2 legs, and 2 arms) before they
lose the game.

In Part 1, we loaded a random word list and picked a
word from it. In Part 2, we wrote the logic for guessing
the letter and displaying that information to the user.
In this exercise, we have to put it all together and add
logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a
starting point. Now add the following features:

-Only let the user guess 6 times, and tell the user how
 many guesses they have left.
-Keep track of the letters the user guessed. If the user
guesses a letter they already guessed, don’t penalize
them - let them guess again.

Optional additions:

-When the player wins or loses, let them start a new game.
-Rather than telling the user "You have 4 incorrect guesses
left", display some picture art for the Hangman. This is
challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of
functions to help you!
"""

import random


def random_word(file_name="sowpods.txt"):
    words = []

    with open(file_name, 'r') as f:
        line = f.readline().strip()
        words.append(line)
        while line:
            line = f.readline().strip()
            words.append(line)

    return words[random.randint(0, len(words) - 1)]


if __name__ == "__main__":
    original = random_word("sowpods.txt")
    word = original
    print("Welcome to Hangman!")
    guessed = '_' * len(word)
    word = list(word)
    guessed = list(guessed)
    letter = input("Guess your letter: ")
    lstGuessed = set()
    try_count = 1
    lives = 6
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        else:
            print(''.join(guessed))
            if letter != '':
                if letter.upper() not in word and letter.upper() not in guessed and letter != '_':
                    print("Incorrect!")
                    lives -= 1
                    print("{} lives left".format(lives))
                    if lives == 0:
                        print("You ran out of lives. The word was {}".format(original))
                        break
                lstGuessed.add(letter.upper())
            try_count += 1
            letter = input("Guess your letter: ")

        if '_' not in guessed:
            print("You won! You have tried {} times. {} lives left.".format(try_count, lives))
            break
