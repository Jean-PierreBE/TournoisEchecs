class CreateGame:

    def prompt_for_result(self,player_A,player_B):
        """Prompt for a score"""
        result = input("Les joueur A " + player_A + " et Joueur B " + player_B + " ont fini .Donnez le score (0 si nul,1 si A gagnant,2 si B gagnant ) : ")
        try:
            return int(result)
        except ValueError:
            return -1

    def prompt_for_continue_round(self):
        """Prompt for a score"""
        response = input("le round est-il terminé (Y/N) ?  ")
        if not response:
            return 'None'
        return response.upper()

    def prompt_for_encode_result(self):
        """Prompt for a score"""
        num_game = input("Pour quel match voulez-vous entrer les scores ?  ")
        try:
            return int(num_game)
        except ValueError:
            return 0