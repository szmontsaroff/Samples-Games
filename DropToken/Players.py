#!/usr/bin/env python3
# Author:  Stephen Montsaroff
# Created: 11/15/2020
"""
Project: DropToken 
File: Players.py
Description:
"""

from collections import defaultdict

class Player(object):

    def __init__(self, name: str):
        """
        Initializes player
        :param name: Player name
        """
        self.__name = name
        self.__games = set()


    def JoinGame(self, game_id: str):
        """
        Handles joining game
        :param game_id:
        :return:
        """
        self.__games.add(game_id)

    def LeaveGame(self, game_id: str):
        """
        Handles leaving of game
        :param game_id:
        :return:
        """
        self.__games.remove(game_id)

    def ListGames(self) -> set:
        """
        List all games player is part of
        :return:
        """
        return self.__games

    def Name(self) -> str:
        """
        Get Player name
        :return:
        """
        return self.__name
        
class PlayersListType(defaultdict):

    def __init__(self):
        defaultdict.__init__(self,lambda: None)

    def AddPlayer(self, player_name:str) -> Player:
        """
        Add player to list of players
        :param player_name:
        :return:
        """
        if self[player_name]:
            # To Do Consider logging this
           pass
        else:
            player = Player(player_name)
            self.update({player_name: player})

        return self[player_name]

    def AllPlayers(self) -> list:
        """
        REturns all players
        :return:
        """
        return list(self.keys())

    def RemovePlayer(self, player_name):
        """
        Removes player from list of players
        :param player_name:
        :return:
        """
        if self[player_name]:
            self[player_name].End()
            del self[player_name]
        else:
            pass
            # To Do Consider logging this
        return

PlayersList = PlayersListType()