from db.db import in_memory
from typing import List
from models.player import Player
from flask import jsonify
import csv

cache = {}


def get_players():
    return in_memory, 200


def get_player(player_id):
    try:
        if player_id in cache:
            return jsonify(cache[player_id])
        for data in in_memory:
            if data.playerID == player_id:
                cache[player_id] = data
                return jsonify(data)
    except Exception as e:
        return {"message": "There was an issue with the server"}, 500
    return {"message": "No such player was found"}, 404


def player_parser(filepath) -> List[Player]:
    players = []
    with open(filepath, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player = Player(
                playerID=row["playerID"],
                birthYear=str(row["birthYear"]) if row["birthYear"] else None,
                birthMonth=int(row["birthMonth"]) if row["birthMonth"] else None,
                birthDay=int(row["birthDay"]) if row["birthDay"] else None,
                birthCountry=str(row["birthCountry"]) if row["birthCountry"] else None,
                birthState=str(row["birthState"]) if row["birthState"] else None,
                birthCity=str(row["birthCity"]) if row["birthCity"] else None,
                deathYear=int(row["deathYear"]) if row["deathYear"] else None,
                deathMonth=int(row["deathMonth"]) if row["deathMonth"] else None,
                deathDay=int(row["deathDay"]) if row["deathDay"] else None,
                deathCountry=str(row["deathCountry"]) if row["deathCountry"] else None,
                deathState=str(row["deathState"]) if row["deathState"] else None,
                deathCity=str(row["deathCity"]) if row["deathCity"] else None,
                nameFirst=str(row["nameFirst"]) if row["nameFirst"] else None,
                nameLast=str(row["nameLast"]) if row["nameLast"] else None,
                nameGiven=str(row["nameGiven"]) if row["nameGiven"] else None,
                weight=int(row["weight"]) if row["weight"] else None,
                height=int(row["height"]) if row["height"] else None,
                bats=str(row["bats"]) if row["bats"] else None,
                throws=str(row["throws"]) if row["throws"] else None,
                debut=str(row["debut"]) if row["debut"] else None,
                finalGame=str(row["finalGame"]) if row["finalGame"] else None,
                retroID=str(row["retroID"]) if row["retroID"] else None,
                bbrefID=str(row["bbrefID"]) if row["bbrefID"] else None,
            )
            players.append(player)
    return players


def load_data():
    try:
        global in_memory
        in_memory = player_parser("Players.csv")
    except Exception as e:
        return {
            "message": f"Something occurred while loading the data into db. error {str(e)}"
        }, 500
    return {"message": f"data loaded, {len(in_memory)}: records were added"}, 200
