import json

import requests
from flask import Flask
from flask_restful import Api, Resource, request

app = Flask(__name__)
api = Api(app)

players = {
    'sachin' :{'name': 'Sachin Tendulkar', 'runs': 34850, 'mathces': 850, 'wickets': 350},
    'ponting':{'name': 'Ricky Ponting', 'runs': 26350, 'matches': 600, 'wickets': '123'},
    'lara': {'name': 'Brain Lara', 'runs': 23300, 'matches': 580, 'wickets': 105}
}

class Players(Resource):

    def get(self, player):
        return {player: players[player]}

    def put(self, player):
        players[player]['team'] = request.form['team']
        return {player: players[player]}

    def patch(self, player):
        data1 = request.json
        data = json.loads(data1)
        players[player][list(data.keys())[0]] = data[list(data.keys())[0]]
        return players[player]

    def post(self, player):
        data1 = request.json
        data = json.loads(data1)
        players[player] = data
        return players

    def delete(self, player):
        if player in players:
            del players[player]
            return {'result': players}
        else:
            return {'KeyError': "Invalid key, Please enter a valid key......"}

api.add_resource(Players, "/getplayer/<string:player>")

if __name__ == '__main__':
    app.run(debug=True)
