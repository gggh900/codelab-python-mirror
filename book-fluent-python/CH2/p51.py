#!/usr/bin/python3

board=[['_']*3 for i in range(3)]
board[1][2]='X'
print(board)

# supposedly not work because outer list made of 3 references to the inner list.

board=[['_'] * 3] * 3
board[1][2] ='X'
print(board)

# 1st one above is equivalent to:

board = []
for i in range(3):
    row=['_'] * 3
    board.append(row)

board[1][2] ='X'
print(board)

# second one above is equivalent to:

row=['_'] * 3
board = []
for i in range(3):
    board.append(row)

board[1][2] ='X'
print(board)



