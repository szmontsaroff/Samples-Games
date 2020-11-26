#!/usr/bin/env python3
# Author:  Stephen Montsaroff
# Created: 11/15/2020
"""
Project: DropToken
File: Server.py
Description:
"""

from flask import Flask, redirect, url_for, request, session, render_template, jsonify, flash
from flask_api import status

import Players
import DropToken
import os

app = Flask(__name__)

app.secret_key = os.urandom(12)
pList = []
gameId = DropToken.GamesList.AddGame(Players.PlayersList.AddPlayer("One"),
                                     Players.PlayersList.AddPlayer("Two"),4,4)
test_game=DropToken.GamesList[gameId]
test_game.Start()

ret = test_game.Update("One",1)
ret = test_game.Update("Two",1)
ret = test_game.Update("One",1)
ret = test_game.Update("Two",4)
ret = test_game.Update("One",3)
ret = test_game.Update("Two",2)
#ret = game.Update("One",'q')
i=1


@app.route('/drop_token', methods=['GET','POST'])
def drop_token_handler():
    if request.method == "GET":
        return jsonify({'games':DropToken.GamesList.AllGames()}), 200
    else:
        players = request.json['players']
        rows = request.json['rows']
        columns = request.json['columns']
        try:
            game_id = DropToken.GamesList.AddGame(Players.PlayersListAdd(players[0]),
                                                  Players.PlayersListAdd(players[1]),rows,columns)
        except Exception as e:
            return f"<h3>Bad Arguments {str(e)}</h3>", 400
        else:
            return jsonify({'gameId':game_id}), 200

@app.route('/drop_token/<game_id>', methods=['GET'])
def get_game(game_id):

    game = DropToken.GamesList[game_id]
    if game is None:
        ret = f"<h3>No game with id = {game_id} found.</h3>"
        return ret, 404
    else:
        players = []
        for player in game.Players():
            player.append(player.Name())
        status = game.RunState()
        winner = game.Winner()
        ret = {"players":players,
               "state": status}
        if winner:
            ret['winner'] = winner
        return jsonify(ret), 200
    return  f"<h3>Malformed Entry.</h3>", 400

@app.route("/drop_token/<game_id>/<player>", methods=["DELETE"])
def quit_game(game_id,player):
    try:
        game = DropToken.GamesList[game_id]
    except Exception as e:
        return (f"<h3>Malformed Entry {str(e)}.</h3>", 400)

    ret = game.Update(player,'q')
    return ret[0],ret[1]

@app.route('/drop_token/<game_id>/<player>', methods=["PUT"])
def make_move(game_id, player):
    try:
        game = DropToken.GamesList[game_id]
    except Exception as e:
        return f"<h3>Malformed Entry {str(e)}.</h3>", 400
    if game is None:
        ret = f"<h3>No game with id = {game_id} found.</h3>"
        return ret, 404
    #Might do a header check to guarantee we have json
    column = request.json['column']
    ret = game.Update(player, int(column))
    return ret[0], ret[1]

@app.route('/drop_token/<game_id>/moves', methods=['GET'])
def get_moves(game_id):
    try:
        game = DropToken.GamesList[game_id]
    except Exception as e:
        return f"<h3>Malformed Entry {str(e)}.</h3>", 400
    if game is None:
        ret = f"<h3>No game with id = {game_id} found.</h3>"
        return ret, 404
    else:
        start = request.args.get('start')
        until = request.args.get('until')
        moves = game.GetMoves()
        if start:
            moves = moves[int(start) - 1:]  # assume one's based argument
        if until:
            moves = moves[:int(until) - 1]
        return jsonify(moves), 200
if __name__ == '__main__':
    app.run(debug=True)
