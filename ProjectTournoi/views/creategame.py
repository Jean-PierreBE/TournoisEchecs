class CreateGame:

    def prompt_for_score(self,player_A,player_B):
        """Prompt for a score"""
        score = input("Les joueur A " + player_A + " et Joueur B " + player_B + " ont fini .Donnez le score (0 si nul,1 si A gagnant,2 si B gagnant ) : ")
        if not score:
            return None
        return score