from ProjectTournoi.models import player as pl
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createendview as cv

import ProjectTournoi.variables as vr
from tinydb import TinyDB

def create_players(self, tournoi):
    """create some players"""
    for num_player in range(vr.NUMBER_PLAYERS):
        lastname = cp.CreatePlayer.prompt_for_lastname(self, num_player)
        firstname = cp.CreatePlayer.prompt_for_firstname(self, num_player)
        birthdate = cp.CreatePlayer.prompt_for_birthdate(self, num_player)
        codesex = cp.CreatePlayer.prompt_for_sex(self, num_player)
        classment = cp.CreatePlayer.prompt_for_classment(self, num_player)

        player = pl.Player(vr.ID_PLAYER + str(num_player + 1), lastname, firstname, birthdate, codesex, classment)
        tournoi.players.append(player)


def choose_players(self, tournoi):
    """create some players"""
    db_players = TinyDB(vr.DB_PLAYERS)
    players_table = db_players.table(vr.DB_PLAYERS)
    players = []
    for row in players_table:
        player = pl.Player(row['player_id'], row['lastname'], row['firstname'], row['birthdate'], row['sex'], row['classment'])
        players.append(player)
    cv.CreateEndView.list_only_players(self, players)
    print(vr.INVITE_CHOOSE_8_PLAYERS)
    for indpt in range(vr.NUMBER_PLAYERS):
        cp.CreatePlayer.prompt_for_continue_players(self)


def create_player(self, play_seq):
    """create 1 player"""
    lastname = cp.CreatePlayer.prompt_for_lastname(self, -1)
    firstname = cp.CreatePlayer.prompt_for_firstname(self, -1)
    birthdate = cp.CreatePlayer.prompt_for_birthdate(self, -1)
    codesex = cp.CreatePlayer.prompt_for_sex(self, -1)
    classment = cp.CreatePlayer.prompt_for_classment(self, -1)
    player = pl.Player(vr.ID_PLAYER + str(play_seq), lastname, firstname, birthdate, codesex, classment)
    self.players.append(player)


def get_players_continue(self):
    resp = True
    while resp:
        response = cp.CreatePlayer.prompt_for_continue_players(self)
        if response.upper() == vr.ANSWER_YES:
            return True
        elif response.upper() == vr.ANSWER_NO:
            return False
        else:
            print(vr.MESSAGE_BAD_ANSWER_Y_OR_N)


def get_players_choose(self):
    resp = True
    while resp:
        response = cp.CreatePlayer.prompt_for_choose_players(self)
        if response < 1 or response > 2:
            print(vr.MESSAGE_BAD_ANSWER_1_OR_2)
        else:
            return response
