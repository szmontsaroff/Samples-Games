#!/usr/bin/env python3
# Author:  Stephen Montsaroff
# Created: 11/17/2020
"""
Project: ticTactoe 
File: tic.py  
Description:
tictactoe game for 2 players
from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
slightly improved by Horst JENS"""

import sys
board = []

for x in range (0, 16) :
    board.append(f"{x + 1:02d}")

playerOneTurn = True
winner = False

def printBoard() :
    ncol =4
    nrow =4
    output = ""
    for row in range(0,nrow):
        for col in range(0,ncol):
            output += f" {board[col+row*nrow ]}"
        output +="\n"
    print(output)

column_point = [12, 13, 14, 15]  # Bottom row
while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    entry = input("Enter colum>> ")
    if entry == 'q':
        sys.exit("Quiting")
    try:
        choice = int(entry)
    except:
        print("please enter a valid field")
        continue
    if choice <1 or choice >4:
        print("please enter a column between 1 and 4")
        continue
    #if board[choice - 1] == ' X' or board [choice-1] == ' O':
    #    print("illegal move, please try again")
    #    continue
    column = choice -1
    if playerOneTurn :
        board[column_point[column]] = ' X'
    else :
        board[column_point[column]] = ' O'
    column_point[column] -= 4

    playerOneTurn = not playerOneTurn

    for x in range (0, 4) :
        y = x * 4
        if (board[y] == board[(y + 1)] and board[y] == board[(y + 2)] and board[y] == board[(y + 3)]) :
            winner = True
            printBoard()
        if (board[x] == board[(x + 4)] and board[x] == board[(x + 8)] and board[x] == board[(x + 12)]):
            winner = True
            printBoard()

    if((board[0] == board[5] and board[0] == board[10] and board[0] == board[15]) or
        (board[12] == board[9] and board[12] == board[6] and board[12] == board[3])):
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
