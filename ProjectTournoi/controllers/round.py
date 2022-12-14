from ProjectTournoi.models import round as rn
from ProjectTournoi.tools.check import get_result_player
from ProjectTournoi.views import create_round as cr
from ProjectTournoi.views import create_end_view as cv
import ProjectTournoi.controllers.game as cgm
import ProjectTournoi.controllers.reports as rep
import ProjectTournoi.controllers.tournament as ctn

import ProjectTournoi.tools.constants as vr


class Controller_round:

    def create_round_begin(self, num_round, tournoi):
        begin_date = cr.CreateRound.prompt_for_begin_date(self, num_round)
        begin_time = cr.CreateRound.prompt_for_begin_time(self, num_round)

        round = rn.Round(vr.ID_ROUND + str(num_round + 1),
                         begin_date, begin_time, '', '', [])
        tournoi.rounds.append(round)

    def get_round_end(self, num_round, tournoi):
        end_date = cr.CreateRound.prompt_for_end_date(self, num_round)

        end_time = cr.CreateRound.prompt_for_end_time(self, num_round)
        round = tournoi.rounds[num_round]
        round.enddate = end_date
        round.endtime = end_time

        for igame in range(vr.NUMBER_GAMES):
            inda = get_result_player(tournoi.players, round.games[igame].player_a)
            indb = get_result_player(tournoi.players, round.games[igame].player_b)
            tournoi.set_result(round.games[igame].result, inda, indb)

        """list of provisional results of tournament"""
        cv.CreateEndView.list_results_tournaments(self, 0, tournoi.date, tournoi.players)


class turning_round:
    def turning_round(self, num_round, tournament):
        """begin round"""
        Controller_round.create_round_begin(self, num_round, tournament)
        """Swiss algorithm"""
        cgm.Controller_game.get_games_swiss(self, num_round, tournament)
        running_game = True
        while running_game:
            """view games"""
            rep.Controller_reports.print_turning_views(self, num_round, tournament)
            """choose number of game to encode or leave the round"""
            running_game, igame = cgm.Controller_game.get_game_choose(self, num_round)
            """encode score"""
            if running_game:
                cgm.Controller_game.get_result(self, tournament.rounds[num_round].games[igame])
        """end round"""
        Controller_round.get_round_end(self, num_round, tournament)
        """select if you want to continue tournament or yes"""
        if num_round == vr.NUMBER_ROUNDS - 1:
            return False
        else:
            return ctn.Controller_tournament.choose_continue_tournament(self)
