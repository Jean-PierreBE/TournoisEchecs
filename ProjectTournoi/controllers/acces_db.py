import jsons
from tinydb import Query, where

from ProjectTournoi.models import player as pl
from ProjectTournoi.models import round as rn
from ProjectTournoi.models import tournament as tn
from ProjectTournoi.models import game as gm

from ProjectTournoi.db import db_players, db_tournament


"""download players"""
def download_players():
    players = []
    for row in db_players:
        player = pl.Player(row['player_id'], row['lastname'], row['firstname'], row['birthdate'], row['sex'],
                           row['classment'])
        players.append(player)
    return players

"""download tournaments"""
def download_tournaments():
    tournaments = []
    for row in db_tournament:
        tournament = tn.Tournament(row['tournament_id'], row['area'], row['date'], row['description'],[], [])
        """create players"""
        for indp in range(len(row['players'])):
            player_sel = pl.Player(row['players'][indp]['player_id'], row['players'][indp]['lastname'],
                                   row['players'][indp]['firstname'],
                                   row['players'][indp]['birthdate'], row['players'][indp]['sex'],
                                   row['players'][indp]['classment'], row['players'][indp]['score'])
            tournament.players.append(player_sel)
        """create rounds"""
        for indr in range(len(row['rounds'])):
            round_sel = rn.Round(row['rounds'][indr]['round_id'], row['rounds'][indr]['begindate'],
                                 row['rounds'][indr]['begintime'], row['rounds'][indr]['enddate'],
                                 row['rounds'][indr]['endtime'],[])
            """create games"""
            for indg in range(len(row['rounds'][indr]['games'])):
                game_sel = gm.Game(row['rounds'][indr]['games'][indg]['game_id'], \
                           row['rounds'][indr]['games'][indg]['player_a'], \
                           row['rounds'][indr]['games'][indg]['player_b'],
                           row['rounds'][indr]['games'][indg]['result'])
                round_sel.games.append(game_sel)

            tournament.rounds.append(round_sel)

        tournaments.append(tournament)

    return tournaments

def insert_players(players):
    serialized_players = jsons.dump(players)
    db_players.insert_multiple(serialized_players)

def update_player(player):
    Playerid = Query()
    db_players.update({'classment': player.classment, 'lastname': player.lastname,
                       'firstname': player.firstname, 'birthdate': player.birthdate,
                       'sex': player.sex}, Playerid.player_id == player.player_id)

def update_tournament(tournament):
    serialized_tournament = jsons.dump(tournament)
    db_tournament.remove(where('tournament_id') == tournament.tournament_id)
    db_tournament.insert(serialized_tournament)

def insert_tournament(tournament):
    serialized_tournament = jsons.dump(tournament)
    db_tournament.insert(serialized_tournament)