import ProjectTournoi.variables as vr
from ProjectTournoi.controllers.tools import check_answer_y_n

class CreateGame:

    def prompt_for_result(self,player_A,player_B):
        """Prompt for a score"""
        result = input(vr.MESSAGE_END_ROUND.format(player_A, player_B))
        try:
            return int(result)
        except ValueError:
            return -1

    def prompt_for_continue_round(self):
        """Prompt for a score"""
        check = False
        while check == False:
            response = input("le round est-il terminé (Y/N) ?  ")
            if not response:
                return vr.ANSWER_NO
            check = check_answer_y_n(response.upper())
            if check == True:
                return response.upper()

    def prompt_for_encode_result(self):
        """Prompt for a score"""
        num_game = input("Pour quel match voulez-vous entrer les scores ?  ")
        try:
            return int(num_game)
        except ValueError:
            return 0