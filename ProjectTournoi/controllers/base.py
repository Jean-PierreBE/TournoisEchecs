"""Define the main controller"""
from typing import List

from ProjectTournoi.models import tournament as tn
from ProjectTournoi.models import player as pl
from ProjectTournoi.models import round as rn
from ProjectTournoi.models import game as gm

from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createround as cr
from ProjectTournoi.views import creategame as cg
from ProjectTournoi.views import createendview as cv

import ProjectTournoi.variables as vr
import ProjectTournoi.controllers.tools as tl


class Controller:
    """Main controller"""

    def __init__(self, ctview, cpview, crview, cgview, cvview):
        # models
        self.players: List[pl.Player] = []
        self.rounds: List[rn.Round] = []
        self.games: List[gm.Game] = []
        # views
        self.ctview = ctview
        self.cpview = cpview
        self.crview = crview
        self.cgview = cgview
        self.vview = cvview

    def get_tournament(self):
        """create tournament"""
        area = ct.CreateTournament.prompt_for_area(self)
        date = ct.CreateTournament.prompt_for_date(self)
        description = ct.CreateTournament.prompt_for_description(self)

        self.tournoi = tn.Tournament(vr.ID_TOURNAMENT, area, date, description, '', '')

    def get_players(self):
        """create some players"""
        for num_player in range(vr.NUMBER_PLAYERS):
            lastname = cp.CreatePlayer.prompt_for_lastname(self, num_player)
            firstname = cp.CreatePlayer.prompt_for_firstname(self, num_player)
            birthdate = cp.CreatePlayer.prompt_for_birthdate(self, num_player)
            codesex = cp.CreatePlayer.prompt_for_sex(self, num_player)
            classment = cp.CreatePlayer.prompt_for_classment(self, num_player)

            player = pl.Player(vr.ID_PLAYER + str(num_player + 1), lastname, firstname, birthdate , codesex, classment)
            self.players.append(player)

    def get_round_begin(self,num_round):
        begin_date = cr.CreateRound.prompt_for_begin_date(self, num_round)
        begin_time = cr.CreateRound.prompt_for_begin_time(self, num_round)

        round = rn.Round(vr.ID_ROUND + str(num_round + 1), begin_date, begin_time, '', '', '')
        self.rounds.append(round)

    def get_round_end(self,num_round):
        end_date = cr.CreateRound.prompt_for_end_date(self, num_round)
        end_time = cr.CreateRound.prompt_for_end_time(self, num_round)

        self.rounds[num_round].enddate = end_date
        self.rounds[num_round].endtime = end_time

    def get_games(self,num_round):
        last_player = 0
        for num_game in range(vr.NUMBER_GAMES):
            pref_game = 'Game_' + str(num_round + 1) + str(num_game + 1)
            player_A = self.tournoi.players[last_player].player_id
            player_B = self.tournoi.players[last_player + 1].player_id
            last_player = last_player + 2
            game = gm.Game(pref_game,player_A, player_B)
            self.games.append(game)

    def get_result(self,num_game, player_A, player_B):
        result = cg.CreateGame.prompt_for_result(self, player_A, player_B)
        inda = tl.get_result_player(self.tournoi.players, player_A)
        indb = tl.get_result_player(self.tournoi.players, player_B)
        self.games[num_game].result = result
        self.tournoi.set_result(result, inda, indb)

    def print_views(self, tournoi):
        """list of tournaments"""
        cv.CreateEndView.list_tournaments(self, tournoi.area, tournoi.date, tournoi.description)
        """list of players"""
        cv.CreateEndView.list_players(self, tournoi.area, tournoi.date, tournoi.players)
        """list of results of games """
        cv.CreateEndView.list_results_rounds(self, tournoi)
        """list of results of tournament"""
        cv.CreateEndView.list_results_tournaments(self, tournoi.area, tournoi.date, tournoi.players)

    def run(self):
        """Run the game."""
        """Initialize tournament"""
        self.get_tournament()
        """Encode players"""
        self.get_players()
        """complete tournament with the list of players"""
        self.tournoi.players = self.players

        """Rounds"""
        for num_round in range(vr.NUMBER_ROUNDS):
            """begin round"""
            self.get_round_begin(num_round)
            """Swiss algorithm"""
            self.get_games(num_round)
            """view games"""
            """encode score"""
            imin = vr.NUMBER_GAMES * (num_round)
            imax = vr.NUMBER_GAMES * (num_round + 1)
            self.rounds[num_round].games = []
            print('imin ' + str(imin))
            print('imax ' + str(imax))
            for igame in range(imin, imax):
                print('igame ' + str(igame))
                self.get_result(igame, self.games[igame].player_A, self.games[igame].player_B)
                self.rounds[num_round].games.append(self.games[igame])
            """end round"""
            self.get_round_end(num_round)

            #self.rounds[num_round].games = self.games
            for i in range(len(self.rounds[num_round].games)):
                print(i, self.rounds[num_round].games[i].game_id)
                print(i, self.rounds[num_round].games[i].player_A)
                print(i, self.rounds[num_round].games[i].player_B)
                print(i, self.rounds[num_round].games[i].result)

        self.tournoi.rounds = self.rounds
        for i in range(len(self.tournoi.rounds)):
            print('i ' + str(i))
            print('self.tournoi.rounds[i].games ' + str(len(self.tournoi.rounds[i].games)))
            for j in range(len(self.tournoi.rounds[i].games)):
                print(i, self.tournoi.rounds[i].games[j].game_id)
                print(i, self.tournoi.rounds[i].games[j].player_A)
                print(i, self.tournoi.rounds[i].games[j].player_B)
                print(i, self.tournoi.rounds[i].games[j].result)
        """Affichage résultat tournoi"""
        self.print_views(self.tournoi)
