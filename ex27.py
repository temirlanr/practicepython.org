"""
In a previous exercise we explored the idea of using
a list of lists as a “data structure” to store information
 about a tic tac toe game. In a tic tac toe game, the
 “game server” needs to know where the Xs and Os are
 in the board, to know whether player 1 or player 2
 (or whoever is X and O won).

There has also been an exercise about drawing the
actual tic tac toe gameboard using text characters.

The next logical step is to deal with handling user
input. When a player (say player 1, who is X) wants
to place an X on the screen, they can’t just click
on a terminal. So we are going to approximate this
clicking simply by asking the user for a coordinate
of where they want to place their piece.

As a reminder, our tic tac toe game is really a list
of lists. The game starts out with an empty game board
like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
The computer asks Player 1 (X) what their move is (
in the format row,col), and say they type 1,3. Then
 the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]
And ask Player 2 for their move, printing an O in
that place.

Things to note:

    -For this exercise, assume that player 1 (the first
player to move) will always be X and player 2 (the
second player) will always be O.
    -Notice how in the example I gave coordinates for
where I want to move starting from (1, 1) instead
 of (0, 0). To people who don’t program, starting
 to count at 0 is a strange concept, so it is better
 for the user experience if the row counts and column
 counts start at 1. This is not required, but whichever
 way you choose to implement this, it should be explained
 to the player.
    -Ask the user to enter coordinates in the form
“row,col” - a number, then a comma, then a number.
Then you can use your Python skills to figure out
which row and column they want their piece to be in.
    -Don’t worry about checking whether someone won the
game, but if a player tries to put a piece in a game
 position where there already is another piece, do
 not allow the piece to go there.
Bonus:

    -For the “standard” exercise, don’t worry about “ending”
the game - no need to keep track of how many squares are
full. In a bonus version, keep track of how many squares
are full and automatically stop asking for moves when
there are no more valid moves.
"""


def check_grid(grid):
    for i in range(3):
        row = {grid[i][0], grid[i][1], grid[i][2]}
        if len(row) == 1 and grid[i][0] != 0:
            return grid[i][0]
    for j in range(3):
        column = {grid[0][j], grid[1][j], grid[2][j]}
        if len(column) == 1 and grid[0][j] != 0:
            return grid[0][j]
    diag1 = {grid[0][0], grid[1][1], grid[2][2]}
    diag2 = {grid[0][2], grid[1][1], grid[2][0]}
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]
    return 0


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

while check_grid(game) == 0:
    print("Player 1!")
    row = int(input("Row: ")) - 1
    column = int(input("Column: ")) - 1
    if game[row][column] == 0:
        game[row][column] = 1
    else:
        print("This cell is already occupied! Enter the values again.")
        continue
    if check_grid(game) != 0:
        print("Player {} wins!!!".format(check_grid(game)))
    print("{0}\n{1}\n{2}".format(*game))
    print("Player 2!")
    row = int(input("Row: ")) - 1
    column = int(input("Column: ")) - 1
    if game[row][column] == 0:
        game[row][column] = 2
    else:
        print("This cell is already occupied! Enter the values again.")
        game[row][column] = 0
        continue
    if check_grid(game) != 0:
        print("Player {} wins!!!".format(check_grid(game)))
    print("{0}\n{1}\n{2}".format(*game))
