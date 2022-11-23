from ProjectTournoi.models import player as pl
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createendview as cv
import ProjectTournoi.controllers.tools as tl

import ProjectTournoi.variables as vr
from tinydb import TinyDB
db_players = TinyDB(vr.DB_PLAYERS)
players_table = db_players.table(vr.DB_PLAYERS)
db_tournament = TinyDB(vr.DB_TOURNAMENT)
tournament_table = db_tournament.table(vr.DB_TOURNAMENT)

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
    players = []
    for row in players_table:
        player = pl.Player(row['player_id'], row['lastname'], row['firstname'], row['birthdate'], row['sex'], row['classment'])
        players.append(player)
    cv.CreateEndView.list_only_players(self, players)
    print(vr.INVITE_CHOOSE_8_PLAYERS)
    for indpt in range(vr.NUMBER_PLAYERS):
        resp = True
        while resp:
            num_play = cp.CreatePlayer.prompt_choose_indice_players(self, indpt + 1)
            if num_play > len(players):
                print(vr.MESSAGE_PLAYER_OUT_OF_RANGE)
            elif(tl.get_result_player(tournoi.players, players[num_play-1].player_id) >= 0 and
                    tl.get_result_player(tournoi.players, players[num_play-1].player_id) < len(players)):
                print(vr.MESSAGE_PLAYER_ALLREADY_SELECTED)
            else:
                player_sel = pl.Player(players[num_play-1].player_id, players[num_play-1].lastname, players[num_play-1].firstname,
                                       players[num_play-1].birthdate, players[num_play-1].sex, players[num_play-1].classment)
                tournoi.players.append(player_sel)
                resp = False
        cv.CreateEndView.list_players(self, tournoi.area, tournoi.date, tournoi.players)


def create_player(self, play_seq):
    """create 1 player"""
    lastname = cp.CreatePlayer.prompt_for_lastname(self, -1)
    firstname = cp.CreatePlayer.prompt_for_firstname(self, -1)
    birthdate = cp.CreatePlayer.prompt_for_birthdate(self, -1)
    codesex = cp.CreatePlayer.prompt_for_sex(self, -1)
    classment = cp.CreatePlayer.prompt_for_classment(self, -1)
    player = pl.Player(vr.ID_PLAYER + str(play_seq), lastname, firstname, birthdate, codesex, classment)
    self.players.append(player)


def update_player(self, player_in):
    """create 1 player"""
    lastname = cp.UpdatePlayer.prompt_for_lastname(self, player_in.lastname)
    firstname = cp.UpdatePlayer.prompt_for_firstname(self, player_in.firstname)
    birthdate = cp.UpdatePlayer.prompt_for_birthdate(self, player_in.birthdate)
    codesex = cp.UpdatePlayer.prompt_for_sex(self, player_in.sex)
    classment = cp.UpdatePlayer.prompt_for_classment(self, player_in.classment)
    player_out = pl.Player(player_in.player_id, lastname, firstname, birthdate, codesex, classment)
    return player_out


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
