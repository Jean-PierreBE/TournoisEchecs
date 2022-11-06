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
        for num_player in range(vr.NUMBER_PLAYERS):
            lastname = cp.CreatePlayer.prompt_for_lastname(self,num_player)
            firstname = cp.CreatePlayer.prompt_for_firstname(self,num_player)
            birthdate = cp.CreatePlayer.prompt_for_birthdate(self,num_player)
            codesex = cp.CreatePlayer.prompt_for_sex(self,num_player)
            classment = cp.CreatePlayer.prompt_for_classment(self,num_player)

            player = pl.Player(vr.ID_PLAYER + str(num_player + 1), lastname,firstname,birthdate ,codesex,classment, '')
            self.players.append(player)

    def get_round_begin(self,num_round):
        begin_date = cr.CreateRound.prompt_for_begin_date(self, num_round)
        begin_time = cr.CreateRound.prompt_for_begin_time(self, num_round)

        round = rn.Round(vr.ID_ROUND + str(num_round + 1),begin_date,begin_time,'','','')
        self.rounds.append(round)

    def get_round_end(self,num_round):
        end_date = cr.CreateRound.prompt_for_end_date(self, num_round)
        end_time = cr.CreateRound.prompt_for_end_time(self, num_round)

        self.rounds[num_round].enddate = end_date
        self.rounds[num_round].endtime = end_time

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

        """Rounds"""
        for num_round in range(vr.NUMBER_ROUNDS):
            """begin round"""
            self.get_round_begin(num_round)
            """Swiss algorithm"""
            """view games"""
            """encode score"""
            """end round"""
            self.get_round_end(num_round)

        self.tournoi.rounds = self.rounds
        for i in range(len(self.tournoi.rounds)):
            print(i,self.tournoi.rounds[i].round_id)
            print(i,self.tournoi.rounds[i].begindate)
            print(i,self.tournoi.rounds[i].begintime)
            print(i,self.tournoi.rounds[i].enddate)
            print(i,self.tournoi.rounds[i].endtime)