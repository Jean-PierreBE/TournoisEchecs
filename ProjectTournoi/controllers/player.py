from ProjectTournoi.models import player as pl
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createendview as cv
import ProjectTournoi.tools.check as tl

import ProjectTournoi.tools.constants as vr

from ProjectTournoi.db import db_players


class Controller_player:

    def choose_players(self, tournoi):
        """create some players"""
        players = []
        if len(db_players) == 0:
            cp.CreatePlayer.prompt_list_players_empty(self)
            return False
        else:
            for row in db_players:
                player = pl.Player(row['player_id'], row['lastname'],
                                   row['firstname'], row['birthdate'],
                                   row['sex'], row['classment'])
                players.append(player)
            cv.CreateEndView.list_only_players(self, players)
            print(vr.MESSAGE_CHOOSE_8_PLAYERS)
            for indpt in range(vr.NUMBER_PLAYERS):
                resp = True
                while resp:
                    num_play = cp.CreatePlayer.\
                        prompt_choose_indice_players(self,
                                                     indpt + 1,
                                                     len(players))
                    if 0 <= tl.get_result_player(tournoi.players,
                                                 players[num_play - 1].
                                                 player_id) \
                            < len(players):
                        print(vr.MESSAGE_PLAYER_ALLREADY_SELECTED)
                    else:
                        player_sel = pl.Player(players[num_play-1].player_id,
                                               players[num_play-1].lastname,
                                               players[num_play-1].firstname,
                                               players[num_play-1].birthdate,
                                               players[num_play-1].sex,
                                               players[num_play-1].classment)
                        tournoi.players.append(player_sel)
                        resp = False
                cv.CreateEndView.list_players(self, tournoi.area,
                                              tournoi.date, tournoi.players)
                return True

    def create_player(self, play_seq):
        """create 1 player"""
        lastname = cp.CreatePlayer.prompt_for_lastname(self,
                                                       vr.LAST_NAME_DEFAULT)
        firstname = cp.CreatePlayer.prompt_for_firstname(self,
                                                         vr.FIRST_NAME_DEFAULT)
        birthdate = cp.CreatePlayer.prompt_for_birthdate(self,
                                                         vr.BIRTHDATE_DEFAULT)
        codesex = cp.CreatePlayer.prompt_for_sex(self, vr.SEX_DEFAULT)
        classment = cp.CreatePlayer.prompt_for_classment(self,
                                                         vr.CLASSMENT_DEFAULT)
        player = pl.Player(vr.ID_PLAYER + str(play_seq), lastname,
                           firstname, birthdate, codesex, classment)
        self.players.append(player)

    def update_player(self, player_in):
        """update 1 player"""
        lastname = cp.CreatePlayer.prompt_for_lastname(self,
                                                       player_in.lastname)
        firstname = cp.CreatePlayer.prompt_for_firstname(self,
                                                         player_in.firstname)
        birthdate = cp.CreatePlayer.prompt_for_birthdate(self,
                                                         player_in.birthdate)
        codesex = cp.CreatePlayer.prompt_for_sex(self,
                                                 player_in.sex)
        classment = cp.CreatePlayer.prompt_for_classment(self,
                                                         player_in.classment)
        player_out = pl.Player(player_in.player_id, lastname,
                               firstname, birthdate, codesex, classment)
        return player_out

    def get_players_continue(self):
        response = cp.CreatePlayer.prompt_for_continue_players(self)
        if response.upper() == vr.ANSWER_YES:
            return True
        elif response.upper() == vr.ANSWER_NO:
            return False

    def update_score_if_replay(self, tournoi):
        """reinit score with 0"""
        for indp in range(len(tournoi.players)):
            tournoi.players[indp].score = 0
        """sum score """
        for indr in range(len(tournoi.rounds)):
            for indg in range(len(tournoi.rounds[indr].games)):
                inda = tl.get_result_player(tournoi.players,
                                            tournoi.rounds[indr].
                                            games[indg].player_a)
                indb = tl.get_result_player(tournoi.players,
                                            tournoi.rounds[indr].
                                            games[indg].player_b)
                tournoi.set_result(tournoi.rounds[indr].games[indg].result,
                                   inda, indb)
