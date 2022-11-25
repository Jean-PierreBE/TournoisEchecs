from ProjectTournoi.models import player as pl
from ProjectTournoi.models import tournament as tn
from ProjectTournoi.db import db_players, db_tournament

def get_result_player(list, element):
    for ind in range(len(list)):
        if list[ind].player_id == element:
            return ind
    return -1

"""Search if player 1 and player 2 played already """


def search_couple(list, element_a, element_b):
    for indr in range(len(list)):
        for indg in range(len(list[indr].games)):
            if list[indr].games[indg].player_a == element_a and list[indr].games[indg].player_b == element_b:
                return True
            if list[indr].games[indg].player_b == element_a and list[indr].games[indg].player_a == element_b:
                return True
    return False

def download_players():
    players = []
    for row in db_players:
        player = pl.Player(row['player_id'], row['lastname'], row['firstname'], row['birthdate'], row['sex'],
                           row['classment'])
        players.append(player)
    return players

def download_tournaments():
    tournaments = []
    for row in db_tournament:
        tournament = tn.Tournament(row['tournament_id'], row['area'], row['date'], row['description'],'','')
        tournaments.append(tournament)
    return tournaments