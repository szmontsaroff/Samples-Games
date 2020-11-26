#!/usr/bin/env python3
# Author:  Stephen Montsaroff
# Created: 11/15/2020
"""
Project: DropToken 
File: DropToken.py
Description:
"""
import uuid
from enums import Enum
import Players
from collections import defaultdict


__Rows = 3
__Columns = 3




class RunStates(Enum):
    NotStarted = 'Not Started'
    InProgress = 'In Progress'
    Done = 'Done'

class Game(object):
    def __init__(self, player1: Players.Player, player2: Players.Player, rows: int, cols: int):
        """
        Initializes game
        :param player1:
        :param player2:
        :param row:
        :param col:
        """
        self.__ID = str(uuid.uuid4().hex)

        player1.JoinGame(self.__ID)
        player2.JoinGame(self.__ID)
        self.__players = [player1, player2]
        self.__cols = cols
        self.__rows = rows

        self.__run_state = RunStates.NotStarted
        self.__winner = None
        self.__text_board = []
        self.__board = []
        self.__moves = []
        self.__column_pointer = [] # where in each column we can enter token
        self.__currentPlayer = 0

    def Start(self):
        """
        Set game to running, if already running, restart
        :return:
        """
        self.__run_state = RunStates.InProgress
        for x in range(0, self.__rows * self.__cols):  # plain text output if we want it now
            self.__text_board.append(f"{str(x + 1):>2}")
            self.__board.append(-1) # State
        self.__currentPlayer = 0
        self.__moves = []
        self.__column_pointer = list(range((self.__rows - 1) * self.__cols, self.__rows * self.__cols))

    def End(self):
        """
        Terminates game
        :return:
        """
        self.__players[0].LeaveGame(self.__ID)
        self.__players[1].LeaveGame(self.__ID)
        self.__run_state = RunStates.Done

    def RunState(self) -> RunStates:
        """
        Returns state of game
        :return:
        """
        return self.__run_state

    def ID(self) -> str:
        """
        Returns unique game ID
        :return:
        """
        return self.__ID

    def Winner(self) -> Players.Player:
        """
        Returns winning player object, or None
        :return:
        """
        return self.__winner

    def Players(self) -> [Players.Player, Players.Player]:
        """
        Returns Games players
        :return:
        [player1, player2]
        """
        return [self.__players ]

    def CurrentPlayer(self) -> Players:
        """
        Returns
        :return: Player object for current Player
        """
        return self.__players[self.__currentPlayer]
    def Player1(self) :
        """
        Returns player1 object
        :return:
        """
        return self.__player[0]


    def Player2(self) :
        """
        Returns player2 object
        :return:
        """
        return self.__player[1]


    def makeTextBoard(self) -> str:
        """
        Makes 'text' board of game state
        :return:
        """
        text_board = ""
        for row in range(0, self.__rows):
            for col in range(0, self.__cols):
                if self.__board[col + row * self.__rows] == -1:
                    text_board += f" {(col + row * self.__rows + 1):02d}"
                elif self.__board[col + row * self.__rows] == 0:
                    text_board += f" X "
                else:
                    text_board += f" O "
            text_board += "\n"
        return text_board

    def makeTableBoard(self) -> str:
        """
        Makes 'html table' board of game state
        :return:
        """
        table_board = "<table>"
        for row in range(0, self.__rows):
            table_board += "<tr>"
            for col in range(0, self.__cols):
                if self.__board[col + row * self.__rows] == -1:
                    table_board += f"<td>{(col + row * self.__rows + 1):02d}</td>"
                elif self.__board[col + row * self.__rows] == 0:
                    table_board += f"<td> X </td>"
                else:
                    table_board += f"<td> O </td>"
            table_board += "</tr>"
        table_board += "</table>"
        return table_board

    def Update(self, player: str, column_choice: int):
        """
        Updates game
        :param player name
        :param column_choice: col to index token -- we only choose columns, unlike tic-tac-toe
        :return:
        """
        if self.__winner or self.__run_state == RunStates.Done:  #no point in playing
            return ["Game {self.__ID} has finished.", 410]

        if player != self.__players[0].Name() and player != self.__players[1].Name():
            return ["Player {player} is not a part of game {self.__ID}",404]

        if player !=  self.__players[self.__currentPlayer].Name():
            return ["Player tried to post when it's not their turn",409]

        if column_choice == 'q':
            move = {"type": "QUIT",
                    "move_number": len(self.__moves) + 1,
                    "player": self.__players[self.__currentPlayer].Name(),
                    }
            self.__moves.append(move)
            self.__run_state = RunStates.Done
            return [self.makeTableBoard(), 202]

        if self.__run_state is RunStates.NotStarted:
            self.Start()


        # check if column is in range, or if full
        if column_choice < 1 or column_choice > self.__cols or self.__column_pointer[column_choice - 1] < 0:
            return 400

        move = {"type": "MOVE",
                "move_number": len(self.__moves) + 1,
                "player": self.__players[self.__currentPlayer].Name(),
                "column": column_choice,
                "row": int(self.__column_pointer[column_choice-1] /self.__rows) + 1
                }
        self.__board[self.__column_pointer[column_choice - 1]] = self.__currentPlayer
        self.__column_pointer[column_choice - 1] -= self.__cols
        self.__moves.append(move)

        if self.__checkForWinner():
            self.__winner = self.__players[self.__currentPlayer]
            self.__run_state = RunStates.Done
        else:
            self.__currentPlayer ^= 1  # toggle to next
        return [self.makeTableBoard(), 200]

    def GetMoves(self) -> list:
        """
        Return a list of dicts containing move information
        :return: 
        """
        return self.__moves

    def __checkForWinner(self) -> bool:
        """
        Checks if winning condition is set, and set winner
        To Do, deal with Cat game
        :return: 
        """
        if self.__winner:
            return True
        
        # Now check winning configurations
            # Check Diag
        if self.__cols == self.__rows:
                  # Don't think a diagonal exists for a rectangle.


            if self.__board[0] != -1 and self.__board[0] == self.__currentPlayer:
                diagDownCheck = True
                for i in range(1,self.__rows):
                    if self.__board[0] != self.__board[i * (self.__rows + 1)]:
                        diagDownCheck = False
                        break
                if diagDownCheck:
                    self.__winner = self.__board[0]
                    return True

            if self.__board[-self.__rows] != -1 and self.__board[-self.__rows] == self.__currentPlayer:
                diagUpCheck = True
                for i in range(1, self.__rows):
                    if self.__board[-self.__rows] != self.__board[i * (self.__rows - 1)]:
                        diagUpCheck = False
                        break
                if diagUpCheck:
                    self.__winner = self.__board[-1]
                    return True

        for row in range (0, self.__rows) :
            offset = row * self.__cols
            row_check = True
            for col in range (1, self.__cols):
                if self.__board[offset] == -1 or self.__board[offset] != self.__board[offset + col]:
                    row_check = False
                    break
            if row_check:  # found row_check winner set it
                self.__winner = self.__board[offset]
                return True

        # Check Columns
        for col in range(0, self.__cols):
            col_check = True
            for row in range(1, self.__rows):
                z = col + row * self.__cols
                if self.__board[col] == -1 or self.__board[col] != self.__board[col + row * self.__cols]:
                    col_check = False
                    break
            if col_check:  # found col_check winner set it
                self.__winner = self.__players[self.__board[col]]
                return True






        return False
    
class GamesListType(defaultdict):

    def __init__(self):
        defaultdict.__init__(self,lambda: None)

    def AddGame(self, player1: Players.Player, player2: Players.Player, rows: int =3, cols: int =3) -> Game:
        game = Game(player1, player2,rows,cols)
        self.update({game.ID():game})
        return game.ID()

    def RemoveGame(self,game_id: str):
        self[game_id].End()
        del self[game_id]

    def AllGames(self) -> list:
        return list(self.keys())

GamesList = GamesListType()