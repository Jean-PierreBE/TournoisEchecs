import ProjectTournoi.variables as vr
from ProjectTournoi.controllers.tools import check_answer_y_n,check_result, check_game

class CreateGame:

    def prompt_for_result(self,player_A,player_B):
        """Prompt for a score"""
        check = False
        while check == False:
            result = input(vr.MESSAGE_END_ROUND.format(player_A, player_B))
            check = check_result(result)
            if check == True:
                return int(result)

    def prompt_for_continue_round(self):
        """Prompt for a score"""
        check = False
        while check == False:
            response = input(vr.MESSAGE_IF_ROUND_FINISHED)
            if not response:
                return vr.ANSWER_NO
            check = check_answer_y_n(response.upper())
            if check == True:
                return response.upper()

    def prompt_for_encode_result(self):
        """Prompt for a score"""
        check = False
        while check == False:
            num_game = input(vr.MESSAGE_NUMBER_MATCH)
            check = check_game(num_game)
            if check == True:
                return int(num_game)