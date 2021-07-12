"""
In 3 previous exercises, we built up a few components
needed to build a Tic Tac Toe game in Python:

1. Draw the Tic Tac Toe game board
2. Checking whether a game board has a winner
3. Handle a player move from user input

The next step is to put all these three components together
to make a two-player Tic Tac Toe game! Your challenge in
this exercise is to use the functions from those previous
exercises all together in the same program to make a two-player
game that you can play with a friend. There are a lot of choices
you will have to make when completing this exercise, so you can
go as far or as little as you want with it.

Here are a few things to keep in mind:

-You should keep track of who won - if there is a winner,
show a congratulatory message on the screen.
-If there are no more moves left, don’t ask for the next
player’s move!

As a bonus, you can ask the players if they want to play again
and keep a running tally of who won more - Player 1 or Player 2.
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


def draw_board(game):
    row = " ---"
    column = "|   "
    p1 = "| X "
    p2 = "| O "
    for i in range(3):
        print(row, end='')
    print('\n', end='')
    for h in range(3):
        for c in range(3):
            if game[h][c] == 0:
                print(column, end='')
            elif game[h][c] == 1:
                print(p1, end='')
            elif game[h][c] == 2:
                print(p2, end='')
        print("|", end='')
        print("\n", end='')
        for w in range(3):
            print(row, end='')
        print('\n', end='')


if __name__ == "__main__":
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    draw_board(game)
    print("Player 1 is X and Player 2 is O.")
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
            draw_board(game)
            break
        #print("{0}\n{1}\n{2}".format(*game)) #This is how the game looks in list
        draw_board(game)
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
        #print("{0}\n{1}\n{2}".format(*game)) #This is how the game looks in list
        draw_board(game)
