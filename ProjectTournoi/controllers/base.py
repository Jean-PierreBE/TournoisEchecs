"""Define the main controller"""
from ProjectTournoi.models import tournament as tn
from ProjectTournoi.models import player as pl
from ProjectTournoi.models import round as rn
from ProjectTournoi.models import game as gm

from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createround as cr
from ProjectTournoi.views import creategame as cg
from ProjectTournoi.views import createendview as cv

import ProjectTournoi.variables as vr
import ProjectTournoi.controllers.tools as tl
import jsons
from tinydb import TinyDB

class Controller:
    """Main controller"""

    def __init__(self, ctview, cpview, crview, cgview, cvview):
        # models
        self.tournois = []
        # views
        self.ctview = ctview
        self.cpview = cpview
        self.crview = crview
        self.cgview = cgview
        self.vview = cvview

    def create_tournament(self):
        """create tournament"""
        area = ct.CreateTournament.prompt_for_area(self)
        date = ct.CreateTournament.prompt_for_date(self)
        description = ct.CreateTournament.prompt_for_description(self)

        new_tournoi = tn.Tournament(vr.ID_TOURNAMENT + str(len(self.tournois)), area, date, description, [], [])
        self.tournois.append(new_tournoi)

    def create_players(self,tournoi):
        """create some players"""
        for num_player in range(vr.NUMBER_PLAYERS):
            lastname = cp.CreatePlayer.prompt_for_lastname(self, num_player)
            firstname = cp.CreatePlayer.prompt_for_firstname(self, num_player)
            birthdate = cp.CreatePlayer.prompt_for_birthdate(self, num_player)
            codesex = cp.CreatePlayer.prompt_for_sex(self, num_player)
            classment = cp.CreatePlayer.prompt_for_classment(self, num_player)

            player = pl.Player(vr.ID_PLAYER + str(num_player + 1), lastname, firstname, birthdate , codesex, classment)
            tournoi.players.append(player)

    def create_round_begin(self, num_round, tournoi):
        begin_date = cr.CreateRound.prompt_for_begin_date(self, num_round)
        begin_time = cr.CreateRound.prompt_for_begin_time(self, num_round)

        round = rn.Round(vr.ID_ROUND + str(num_round + 1), begin_date, begin_time, '', '', [])
        tournoi.rounds.append(round)

    def get_round_end(self,num_round, tournoi):
        end_date = cr.CreateRound.prompt_for_end_date(self, num_round)

        end_time = cr.CreateRound.prompt_for_end_time(self, num_round)
        round = tournoi.rounds[num_round]
        round.enddate = end_date
        round.endtime = end_time

        for igame in range(vr.NUMBER_GAMES):
            inda = tl.get_result_player(tournoi.players, round.games[igame].player_a)
            indb = tl.get_result_player(tournoi.players, round.games[igame].player_b)
            tournoi.set_result(round.games[igame].result, inda, indb)

        """list of provisional results of tournament"""
        cv.CreateEndView.list_results_tournaments(self,0, tournoi.area, tournoi.date, tournoi.players)

    def get_game_choose(self,num_round):
        resp = True
        while resp:
            response = cg.CreateGame.prompt_for_continue_round(self)
            if response.upper() == vr.ANSWER_YES:
                return False, None
            elif response.upper() == vr.ANSWER_NO:
                num_game = cg.CreateGame.prompt_for_encode_result(self)
                if num_game < 1 or num_game > vr.NUMBER_GAMES:
                    print(vr.MESSAGE_WRONG_GAME)
                else:
                    return True, int(num_game) - 1
            else:
                print(vr.MESSAGE_BAD_ANSWER)

    def get_games_swiss(self,num_round, tournoi):
        """first round"""
        if num_round == 0:
            sorted_player = sorted(tournoi.players,key=lambda e:e.classment, reverse=True)
            last_player = 0
            for num_game in range(vr.NUMBER_GAMES):
                pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
                player_a = sorted_player[last_player].player_id
                player_b = sorted_player[last_player + 4].player_id
                last_player = last_player + 1
                game = gm.Game(pref_game,player_a, player_b)
                tournoi.rounds[num_round].games.append(game)
        else:
            sorted_player = sorted(tournoi.players, key=lambda e:(e.score,e.classment), reverse=True)
            last_player = 0
            """search precedent game"""
            already_played = tl.search_couple(tournoi.rounds, sorted_player[0].player_id,
                                       sorted_player[1].player_id)
            for num_game in range(vr.NUMBER_GAMES):
                pref_game = vr.ID_GAME + str(num_round + 1) + str(num_game + 1)
                if already_played and num_game < 2:
                    if num_game == 0:
                        ind_playa =  0
                        ind_playb =  2
                    elif num_game == 1:
                        ind_playa = 1
                        ind_playb = 3
                        last_player = 4
                else:
                    ind_playa = last_player
                    ind_playb = last_player + 1
                    last_player = last_player + 2
                player_a = sorted_player[ind_playa].player_id
                player_b = sorted_player[ind_playb].player_id
                game = gm.Game(pref_game, player_a, player_b)
                tournoi.rounds[num_round].games.append(game)

    def get_result(self,game):
        resp = True
        while resp:
            result = cg.CreateGame.prompt_for_result(self, game.player_a, game.player_b)
            if result < 0 or result > 2:
                print(vr.MESSAGE_WRONG_RESULT)
            else:
                game.result = result
                resp = False

    def print_turning_views(self, num_round, tournoi):
        """list of tournaments"""
        cv.CreateEndView.list_turning_round(self, num_round, tournoi)

    def print_end_views(self, tournoi):
        """list of tournaments"""
        cv.CreateEndView.list_tournaments(self, tournoi.area, tournoi.date, tournoi.description)
        """list of players"""
        cv.CreateEndView.list_players(self, tournoi.area, tournoi.date, tournoi.players)
        """list of rounds"""
        cv.CreateEndView.list_rounds(self, tournoi)
        """list of results of games """
        cv.CreateEndView.list_results_rounds(self, tournoi)
        """list of results of tournament"""
        cv.CreateEndView.list_results_tournaments(self, 1, tournoi.area, tournoi.date, tournoi.players)

    def run(self):
        """Run the game."""
        """Initialize tournament"""
        self.create_tournament()
        # liste des tournois
        # demander de créer ou gérer un tournoi existant
        # tournoi = self.tournois[indice choisi]
        current_tournament = self.tournois[0]
        """Encode players"""
        self.create_players(current_tournament)

        """Rounds"""
        for num_round in range(vr.NUMBER_ROUNDS):
            """begin round"""
            self.create_round_begin(num_round, current_tournament)
            """Swiss algorithm"""
            self.get_games_swiss(num_round, current_tournament)
            running_game = True

            while running_game:
                """view games"""
                self.print_turning_views(num_round, current_tournament)
                """choose number of game to encode or leave the round"""
                running_game, igame = self.get_game_choose(num_round)
                """encode score"""
                if running_game:
                    self.get_result(current_tournament.rounds[num_round].games[igame])
            """end round"""
            self.get_round_end(num_round, current_tournament)

        """Affichage résultat tournoi"""
        self.print_end_views(current_tournament)
        """serialize object"""
        serialized_tournament = jsons.dump(current_tournament)
        db = TinyDB('db.json')
        tournament_table = db.table('tournament')
        tournament_table.truncate()  # clear the table first
        tournament_table.insert(serialized_tournament)

        current_tournament.serialize()