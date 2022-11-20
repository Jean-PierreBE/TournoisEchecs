from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.models import tournament as tn

import ProjectTournoi.variables as vr

def create_tournament(self):
    """create tournament"""
    area = ct.CreateTournament.prompt_for_area(self)
    date = ct.CreateTournament.prompt_for_date(self)
    description = ct.CreateTournament.prompt_for_description(self)

    new_tournoi = tn.Tournament(vr.ID_TOURNAMENT + str(len(self.tournois)), area, date, description, [], [])
    self.tournois.append(new_tournoi)