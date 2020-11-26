#!/usr/bin/env python3
# Author:  Stephen Montsaroff
# Created: 11/18/2020
"""
Project: DropToken 
File: cmdLine.py  
Description:
"""
import DropToken
import Players
import sys

if __name__ == "__main__":
    game = DropToken.Game(Players.Player("One"),Players.Player("Two"),4,4)
    game.Start()

    while not game.Winner():
        print(game.makeTextBoard())
        print(f"Player '{game.CurrentPlayer().Name()}':")
        entry = input("Enter column>> ")
        if entry == 'q':
            sys.exit("Quiting")
        try:
            choice = int(entry)
        except:
            print("please enter a valid field")
            continue
        ret = game.Update(game.CurrentPlayer().Name(),choice)
        if ret[1] != 200:
            print("please enter a valid field")
            continue
        else:
            if game.Winner():
                print(f"The winner is '{game.Winner().Name()}'")
                print(game.makeTextBoard())
                sys.exit(0)