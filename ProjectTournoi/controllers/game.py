from ProjectTournoi.models import game as gm
from ProjectTournoi.views import creategame as cg
import ProjectTournoi.tools.constants as vr

class Controller_game:

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
            """search precedent game"""
            """
            history = {
                        player_1 : [player_2,player_4], 
                        player_2 : [player_1,player_5],...
                    }
            """
            history = {player.player_id: [] for player in tournoi.players}
            for round in tournoi.rounds:
                for game in round.games:
                    history[game.player_a].append(game.player_b)
                    history[game.player_b].append(game.player_a)
            affected_players = []
            num_game = 0
            for player in sorted_players:
                for adversaire in sorted_players:
                    if (adversaire.player_id != player.player_id) and (adversaire.player_id not in history[player.player_id]) and (adversaire.player_id not in affected_players)\
                            and (player.player_id not in affected_players):
                        pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
                        game = gm.Game(pref_game, player.player_id, adversaire.player_id)
                        tournoi.rounds[num_round].games.append(game)
                        num_game += 1
                        affected_players.append(player.player_id)
                        affected_players.append(adversaire.player_id)
            """check if all players affected"""
            if len(affected_players) < vr.NUMBER_PLAYERS:
                miss_player = []
                for player in sorted_players:
                    if player.player_id not in affected_players:
                        miss_player.append(player.player_id)
                """get names of the last player"""
                pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
                game = gm.Game(pref_game, miss_player[0], miss_player[1])
                tournoi.rounds[num_round].games.append(game)
            return True

    def get_game_choose(self, num_round):
        response = cg.CreateGame.prompt_for_continue_round(self)
        if response.upper() == vr.ANSWER_YES:
            return False, None
        elif response.upper() == vr.ANSWER_NO:
            num_game = cg.CreateGame.prompt_for_encode_result(self)
            return True, int(num_game) - 1

    def get_result(self, game):
        game.result = cg.CreateGame.prompt_for_result(self, game.player_a, game.player_b)
