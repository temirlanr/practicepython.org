"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""


def rps(fp, sp):

    if fp == sp and (
            fp == "scissors" or fp == "rock" or fp == "paper") and (
            sp == "scissors" or sp == "rock" or sp == "paper"):
        return "draw"
    elif (fp == "rock" and sp == "scissors") or (
            fp == "scissors" and sp == "paper") or (
            fp == "paper" and sp == "rock"):
        return "player 1 wins"
    elif (sp == "rock" and fp == "scissors") or (
            sp == "scissors" and fp == "paper") or (
            sp == "paper" and fp == "rock"):
        return "player 2 wins"
    else:
        return 'type "rock", "paper" or "scissors" please'


cmd = input('type \"play\" to play: ')

while cmd != "quit":
    p1 = input("Player 1: rock-paper-scissors... ")
    p2 = input("Player 2: rock-paper-scissors... ")
    print(rps(p1, p2))
    cmd = input('type "quit" to quit or type anything to play: ')
