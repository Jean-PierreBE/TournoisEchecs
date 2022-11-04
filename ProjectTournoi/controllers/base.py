"""Define the main controller"""

from ProjectTournoi.models import tournament as tn
from ProjectTournoi.views import createtournament as ct

class Controller:
    """Main controller"""

    def __init__(self,view):
        # models

        # views
        self.view = view

    def get_tournament(self):
        """create area"""
        area = ct.CreateTournament.prompt_for_area(self)
        date = ct.CreateTournament.prompt_for_date(self)
        description = ct.CreateTournament.prompt_for_description(self)

        self.tournoi = tn.Tournament('tourno01',area,date,description,'','')


    def run(self):
        """Run the game."""
        self.get_tournament()
        print('area : ' + self.tournoi.area)