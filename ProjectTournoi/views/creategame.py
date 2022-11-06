import datetime as dt
import ProjectTournoi.variables as vr

class CreateGame:

    def prompt_for_score(self):
        """Prompt for a begin date"""
        score = input("Entrez le score : ")
        if not score:
            return None
        return score