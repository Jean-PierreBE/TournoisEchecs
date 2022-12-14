from ProjectTournoi.views import create_tournament as ct
from ProjectTournoi.models import tournament as tn

from ProjectTournoi.tools.constants import ID_TOURNAMENT, ANSWER_NO, ANSWER_YES


class Controller_tournament:

    def create_tournament(self, num_id):
        """create tournament"""
        area = ct.CreateTournament.prompt_for_area(self)
        date = ct.CreateTournament.prompt_for_date(self)
        description = ct.CreateTournament.prompt_for_description(self)

        self.current_tournament = tn.Tournament(ID_TOURNAMENT +
                                                str(num_id + 1),
                                                area,
                                                date,
                                                description, [], [])

    def choose_continue_tournament(self):
        resp = True
        while resp:
            response = ct.CreateTournament.prompt_for_continue_tournament(self)
            if response.upper() == ANSWER_YES:
                return True
            elif response.upper() == ANSWER_NO:
                return False

    def continue_another_tournament(self):
        resp = True
        while resp:
            response = ct.CreateTournament.prompt_continue_another_tournament(self)
            if response.upper() == ANSWER_YES:
                return True
            elif response.upper() == ANSWER_NO:
                return False
