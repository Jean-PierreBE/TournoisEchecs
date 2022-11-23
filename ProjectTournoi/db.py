"""Entry point"""
from tinydb import TinyDB
import ProjectTournoi.variables as vr

db_players = TinyDB(vr.DB_PLAYERS)
players_table = db_players.table(vr.DB_PLAYERS)
db_tournament = TinyDB(vr.DB_TOURNAMENT)
tournament_table = db_tournament.table(vr.DB_TOURNAMENT)
