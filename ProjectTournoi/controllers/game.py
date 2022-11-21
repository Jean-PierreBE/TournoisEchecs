from ProjectTournoi.models import game as gm
import ProjectTournoi.controllers.tools as tl
from ProjectTournoi.views import creategame as cg

import ProjectTournoi.variables as vr


def get_games_swiss(self, num_round, tournoi):
    """first round"""
    if num_round == 0:
        sorted_player = sorted(tournoi.players, key=lambda e: e.classment, reverse=True)
        last_player = 0
        for num_game in range(vr.NUMBER_GAMES):
            pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
            player_a = sorted_player[last_player].player_id
            player_b = sorted_player[last_player + 4].player_id
            last_player = last_player + 1
            game = gm.Game(pref_game, player_a, player_b)
            tournoi.rounds[num_round].games.append(game)
    else:
        sorted_player = sorted(tournoi.players, key=lambda e: (e.score, e.classment), reverse=True)
        last_player = 0
        """search precedent game"""
        already_played = tl.search_couple(tournoi.rounds, sorted_player[0].player_id,
                                          sorted_player[1].player_id)
        for num_game in range(vr.NUMBER_GAMES):
            pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
            if already_played and num_game < 2:
                if num_game == 0:
                    ind_playa = 0
                    ind_playb = 2
                elif num_game == 1:
                    ind_playa = 1
                    ind_playb = 3
                    last_player = 4
            else:
                ind_playa = last_player
                ind_playb = last_player + 1
                last_player = last_player + 2
            player_a = sorted_player[ind_playa].player_id
            player_b = sorted_player[ind_playb].player_id
            game = gm.Game(pref_game, player_a, player_b)
            tournoi.rounds[num_round].games.append(game)

def get_game_choose(self,num_round):
    resp = True
    while resp:
        response = cg.CreateGame.prompt_for_continue_round(self)
        if response.upper() == vr.ANSWER_YES:
            return False, None
        elif response.upper() == vr.ANSWER_NO:
            num_game = cg.CreateGame.prompt_for_encode_result(self)
            if num_game < 1 or num_game > vr.NUMBER_GAMES:
                print(vr.MESSAGE_WRONG_GAME)
            else:
                return True, int(num_game) - 1
        else:
            print(vr.MESSAGE_BAD_ANSWER_Y_OR_N)

def get_result(self,game):
    resp = True
    while resp:
        result = cg.CreateGame.prompt_for_result(self, game.player_a, game.player_b)
        if result < 0 or result > 2:
            print(vr.MESSAGE_WRONG_RESULT)
        else:
            game.result = result
            resp = False
