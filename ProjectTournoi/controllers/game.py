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
        sorted_players = sorted(tournoi.players, key=lambda e: (e.score, e.classment), reverse=True)
        last_player = 0
        """search precedent game"""
        """
        history = {
                    player_1 : [player_2,player_4], 
                    player_2 : [player_1,player_5],...
                }
        """
        history = {player.player_id : [] for player in tournoi.players}
        for round in tournoi.rounds:
            for game in round.games:
                history[game.player_a].append(game.player_b)
                history[game.player_b].append(game.player_a)

        affected_players = []
        num_game = 0
        for player in sorted_players:
            for adversaire in sorted_players:
                if (adversaire != player) and (adversaire not in history[player.player_id]) and (adversaire not in affected_players):

                    pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
                    game = gm.Game(pref_game, player, adversaire)
                    tournoi.rounds[num_round].games.append(game)
                    num_game += 1
                    affected_players.append(player)
                    affected_players.append(adversaire)


def get_game_choose(self,num_round):
    response = cg.CreateGame.prompt_for_continue_round(self)
    if response.upper() == vr.ANSWER_YES:
        return False, None
    elif response.upper() == vr.ANSWER_NO:
        num_game = cg.CreateGame.prompt_for_encode_result(self)
        return True, int(num_game) - 1

def get_result(self, game):
    game.result = cg.CreateGame.prompt_for_result(self, game.player_a, game.player_b)

