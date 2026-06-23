
from const import *
from util import *

walls = [(2,3),(5,5),(5,7),(2,7),(5,9)]

board= []


p_row = 9
p_col = 9

for i in range(Rows):
    row = ["."] * Col
    board.append(row)

print("\n" * 40)
while True:
    print("move the P to top-left corner")
    
    for i in range(Rows):
        for j in range(Col):
            board[i][j] = "."

    for wall in walls:
        board[wall[0]][wall[1]] = "X"

    board[p_row][p_col] = "P"

    print_board(board)


    move = input("enter your move(W/A/S/D): ")


    new_row = p_row
    new_col = p_col

    if move.upper() == "W":
        new_row -= 1
    elif move.upper() == "A":
        new_col -= 1
    elif move.upper() == "S":
        new_row += 1
    elif move.upper() == "D":
        new_col += 1

    if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 9:
        print("Invalid Move")
    elif board[new_row][new_col] == "X":
        print("Invalid Move: wall")
    else:
        p_row = new_row
        p_col = new_col 