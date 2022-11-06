"""Define the main controller"""
from typing import List
"""Models"""
from ProjectTournoi.models import tournament as tn
from ProjectTournoi.models import player as pl
from ProjectTournoi.models import round as rn
from ProjectTournoi.models import game as gm
"""views"""
from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createround as cr
from ProjectTournoi.views import creategame as cg
"""other packages"""
import ProjectTournoi.variables as vr
class Controller:
    """Main controller"""

    def __init__(self,ctview,cpview,crview):
        # models
        self.players: List[pl.Player] = []
        self.rounds: List[rn.Round] = []
        self.games: List[gm.Game] = []
        # views
        self.ctview = ctview
        self.cpview = cpview
        self.crview = crview

    def get_tournament(self):
        """create tournament"""
        area = ct.CreateTournament.prompt_for_area(self)
        date = ct.CreateTournament.prompt_for_date(self)
        description = ct.CreateTournament.prompt_for_description(self)

        self.tournoi = tn.Tournament(vr.ID_TOURNAMENT,area,date,description,'','')

    def get_players(self):
        """create some players"""
        for i in range(vr.NUMBER_PLAYERS):
            lastname = cp.CreatePlayer.prompt_for_lastname(self,i)
            firstname = cp.CreatePlayer.prompt_for_firstname(self,i)
            birthdate = cp.CreatePlayer.prompt_for_birthdate(self,i)
            codesex = cp.CreatePlayer.prompt_for_sex(self,i)
            classment = cp.CreatePlayer.prompt_for_classment(self,i)

            player = pl.Player(vr.ID_PLAYER + str(i + 1), lastname,firstname,birthdate ,codesex,classment, '')
            self.players.append(player)

    def run(self):
        """Run the game."""
        """Initialize tournament"""
        self.get_tournament()
        #print('area : ' + self.tournoi.area)
        """Encode players"""
        self.get_players()
        """complete tournament with the list of players"""
        self.tournoi.players = self.players

        for i in range(len(self.tournoi.players)):
            print(i,self.tournoi.players[i].player_id)
            print(i,self.tournoi.players[i].lastname)
            print(i,self.tournoi.players[i].firstname)
            print(i,self.tournoi.players[i].birthdate)
            print(i,self.tournoi.players[i].sex)
            print(i,self.tournoi.players[i].classment)

