"""definition of databases"""
from tinydb import TinyDB

"""DataBase"""
DB_TOURNAMENT = 'db_Tournament.json'
DB_PLAYERS = 'db_Players.json'

db_players = TinyDB(DB_PLAYERS)
db_tournament = TinyDB(DB_TOURNAMENT)
