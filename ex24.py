"""
Time for some fake graphics! Let’s say we want to
draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic tac toe). Obviously,
they come in many other sizes (8x8 for chess, 19x19
for Go, and many more).

Ask the user what size game board they want to draw,
and draw it for them to the screen using Python’s
print statement.

Remember that in Python 3, printing to the screen
is accomplished by

  print("Thing to show on screen")
"""


def board(width, height):
    row = " ---"
    column = "|   "
    for i in range(width):
        print(row, end='')
    print('\n', end='')
    for h in range(height):
        for c in range(width+1):
            print(column, end='')
        print("\n", end='')
        for w in range(width):
            print(row, end='')
        print('\n', end='')


board(9, 9)
