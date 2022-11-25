from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.models import tournament as tn

from ProjectTournoi.variables import ID_TOURNAMENT

def create_tournament(self, num_id):
    """create tournament"""
    area = ct.CreateTournament.prompt_for_area(self)
    date = ct.CreateTournament.prompt_for_date(self)
    description = ct.CreateTournament.prompt_for_description(self)

    self.current_tournament = tn.Tournament(ID_TOURNAMENT + str(num_id + 1), area, date, description, [], [])