"""Define the main controller"""
import ProjectTournoi.controllers.Reports as rep
import ProjectTournoi.controllers.tournament as ctn
import ProjectTournoi.controllers.game as cgm
import ProjectTournoi.controllers.round as rnd
import ProjectTournoi.controllers.player as ply

from ProjectTournoi.views import createendview as cv
from ProjectTournoi.views import createplayer as cp
from ProjectTournoi.views import createtournament as ct
from ProjectTournoi.variables import NUMBER_ROUNDS
import ProjectTournoi.controllers.tools as tl

import jsons
from tinydb import Query
from ProjectTournoi.db import db_players, db_tournament

class Controller:
    """Main controller"""


    def __init__(self, ctview, cpview, crview, cgview, cvview):
        # models
        self.tournois = []
        self.players = []
        # views
        self.ctview = ctview
        self.cpview = cpview
        self.crview = crview
        self.cgview = cgview
        self.vview = cvview

    def run_create_players(self):
        encode_players = True
        play_seq = len(db_players)
        while encode_players:
            """Encode players"""
            play_seq += 1
            ply.create_player(self, play_seq)
            encode_players = ply.get_players_continue(self)
        serialized_players = jsons.dump(self.players)
        db_players.insert_multiple(serialized_players)
        self.players.clear()

    def run_update_players(self):
        encode_players = True
        players = tl.download_players()
        cv.CreateEndView.list_only_players(self, players)
        while encode_players:
            """Encode players"""
            num_play = cp.CreatePlayer.prompt_choose_indice_players(self, -1, len(players))
            player_out = ply.update_player(self, players[num_play-1])
            Playerid = Query()
            db_players.update({'classment': player_out.classment, 'lastname': player_out.lastname,
                                'firstname': player_out.firstname, 'birthdate': player_out.birthdate,
                               'sex': player_out.sex}, Playerid.player_id == player_out.player_id)
            encode_players = ply.get_players_continue(self)


    def run_update_tournoi(self):
        # list of tournaments
        update_tournament = True
        while update_tournament:
            tournois = tl.download_tournaments()
            cv.CreateEndView.list_only_tournaments(self, tournois)
            """Choose tournament"""
            ind_tournament = ct.CreateTournament.prompt_choose_tournament(self, len(tournois))
            tournament = tournois[ind_tournament - 1]
            """choose round to restart"""
            round_deb = ct.CreateTournament.prompt_choose_round_deb(self, len(tournament.rounds) + 1)
            running_tournament = True
            while running_tournament:
                for num_round in range(NUMBER_ROUNDS):
                    print("num_round " + str(num_round))
                    running_game = True
                    while running_game:
                        running_game, igame = cgm.get_game_choose(self, num_round)
                    running_tournament = ctn.choose_continue_tournament(self)
                    if running_tournament is False:
                        break
            update_tournament = ctn.continue_another_tournament(self)

    def run_create_tournoi(self):
        ctn.create_tournament(self, len(db_tournament))
        """choose players from a list"""
        ply.choose_players(self, self.current_tournament)
        """Tournament"""
        running_tournament = True
        """Rounds"""
        for num_round in range(NUMBER_ROUNDS):
            """begin round"""
            rnd.create_round_begin(self, num_round, self.current_tournament)
            """Swiss algorithm"""
            cgm.get_games_swiss(self, num_round, self.current_tournament)
            running_game = True

            while running_game:
                """view games"""
                rep.print_turning_views(self, num_round, self.current_tournament)
                """choose number of game to encode or leave the round"""
                running_game, igame = cgm.get_game_choose(self, num_round)
                """encode score"""
                if running_game:
                    cgm.get_result(self, self.current_tournament.rounds[num_round].games[igame])
            """end round"""
            rnd.get_round_end(self, num_round, self.current_tournament)
            """select if you want to continue tournament or yes"""
            running_tournament = ctn.choose_continue_tournament(self)
            if running_tournament is False:
                break

        """Affichage résultat tournoi"""
        rep.print_end_views(self, self.current_tournament)
        """serialize object"""
        serialized_tournament = jsons.dump(self.current_tournament)
        db_tournament.insert(serialized_tournament)

    def run_report_players_alph(self):
        """reports"""
        rep.print_players_order_alphabetics(self)
    def run_report_players_classment(self):
        rep.print_players_order_classment(self)

    def run_report_tournament(self):
        rep.print_all_tournaments(self)
