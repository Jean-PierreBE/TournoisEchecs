"""management of games"""
import ProjectTournoi.tools.constants as vr
from ProjectTournoi.tools.check import check_answer_y_n, check_result, check_game


class CreateGame:

    def prompt_for_result(self, player_A, player_B):
        """Prompt for the result of the game"""
        check = False
        while check is False:
            result = input(vr.MESSAGE_END_ROUND.format(player_A, player_B))
            check = check_result(result)
            if check is True:
                return int(result)

    def prompt_for_continue_round(self):
        """Prompt to continue the round or no"""
        check = False
        while check is False:
            response = input(vr.MESSAGE_IF_ROUND_FINISHED)
            check = check_answer_y_n(response.upper())
            if check is True:
                return response.upper()

    def prompt_for_encode_result(self):
        """Prompt to select the game to encode the result"""
        check = False
        while check is False:
            num_game = input(vr.MESSAGE_NUMBER_MATCH)
            check = check_game(num_game)
            if check is True:
                return int(num_game)
