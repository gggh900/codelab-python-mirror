#!/usr/bin/python3

board=[['_']*3 for i in range(3)]
print(board)
board[1][2]='X'
print(board)

# supposedly not work because outer list made of 3 references to the inner list.

board1=[['_'] * 3] * 3
print(board1)
board1[1][2] ='X'
print(board1)
