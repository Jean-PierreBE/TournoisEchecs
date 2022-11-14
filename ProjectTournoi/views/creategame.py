class CreateGame:

    def prompt_for_result(self,player_A,player_B):
        """Prompt for a score"""
        result = input("Les joueur A " + player_A + " et Joueur B " + player_B + " ont fini .Donnez le score (0 si nul,1 si A gagnant,2 si B gagnant ) : ")
        if not result:
            return None
        return int(result)

    def prompt_for_continue_round(self):
        """Prompt for a score"""
        response = input("le round est-il terminé (Y/N) ?  ")
        if not response:
            return 'N'
        return response.upper()

    def prompt_for_encode_result(self):
        """Prompt for a score"""
        num_game = input("Pour quel match voulez-vous entrer les scores ?  ")
        if not num_game:
            return None
        return int(num_game)