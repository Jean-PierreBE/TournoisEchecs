from ProjectTournoi.models import round as rn
import ProjectTournoi.controllers.tools as tl
from ProjectTournoi.views import createround as cr
from ProjectTournoi.views import createendview as cv

import ProjectTournoi.variables as vr

def create_round_begin(self, num_round, tournoi):
    begin_date = cr.CreateRound.prompt_for_begin_date(self, num_round)
    begin_time = cr.CreateRound.prompt_for_begin_time(self, num_round)

    round = rn.Round(vr.ID_ROUND + str(num_round + 1), begin_date, begin_time, '', '', [])
    tournoi.rounds.append(round)


def get_round_end(self, num_round, tournoi):
    end_date = cr.CreateRound.prompt_for_end_date(self, num_round)

    end_time = cr.CreateRound.prompt_for_end_time(self, num_round)
    round = tournoi.rounds[num_round]
    round.enddate = end_date
    round.endtime = end_time

    for igame in range(vr.NUMBER_GAMES):
        inda = tl.get_result_player(tournoi.players, round.games[igame].player_a)
        indb = tl.get_result_player(tournoi.players, round.games[igame].player_b)
        tournoi.set_result(round.games[igame].result, inda, indb)

    """list of provisional results of tournament"""
    cv.CreateEndView.list_results_tournaments(self, 0, tournoi.area, tournoi.date, tournoi.players)