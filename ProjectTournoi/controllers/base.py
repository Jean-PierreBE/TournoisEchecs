"""Define the main controller"""
import ProjectTournoi.controllers.Reports as rep
import ProjectTournoi.controllers.tournament as ctn
import ProjectTournoi.controllers.game as cgm
import ProjectTournoi.controllers.round as rnd
import ProjectTournoi.controllers.player as ply

from ProjectTournoi.views import createendview as cv
from ProjectTournoi.views import createplayer as cp

import ProjectTournoi.variables as vr
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

    def run_update_players(self):
        encode_players = True
        players = tl.download_players()
        cv.CreateEndView.list_only_players(self, players)
        while encode_players:
            """Encode players"""
            num_play = cp.CreatePlayer.prompt_choose_indice_players(self, -1)
            player_out = ply.update_player(self, players[num_play-1])
            Playerid = Query()
            db_players.update({'classment': player_out.classment,'lastname': player_out.lastname,
                                'firstname': player_out.firstname, 'birthdate': player_out.birthdate,
                               'sex': player_out.sex}, Playerid.player_id == player_out.player_id)
            encode_players = ply.get_players_continue(self)

    def run_create_tournoi(self):
        """Run the game."""
        if len(self.tournois) == 0:
            pass
        """Initialize tournament"""
        ctn.create_tournament(self)
        # liste des tournois
        # demander de créer ou gérer un tournoi existant
        # tournoi = self.tournois[indice choisi]
        current_tournament = self.tournois[0]
        """choose players from a list"""
        ply.choose_players(self, current_tournament)

        """Rounds"""
        for num_round in range(vr.NUMBER_ROUNDS):
            """begin round"""
            rnd.create_round_begin(self, num_round, current_tournament)
            """Swiss algorithm"""
            cgm.get_games_swiss(self, num_round, current_tournament)
            running_game = True

            while running_game:
                """view games"""
                rep.print_turning_views(self, num_round, current_tournament)
                """choose number of game to encode or leave the round"""
                running_game, igame = cgm.get_game_choose(self, num_round)
                """encode score"""
                if running_game:
                    cgm.get_result(self, current_tournament.rounds[num_round].games[igame])
            """end round"""
            rnd.get_round_end(self, num_round, current_tournament)

        """Affichage résultat tournoi"""
        rep.print_end_views(self, current_tournament)
        """serialize object"""
        serialized_tournament = jsons.dump(current_tournament)
        db_tournament.insert(serialized_tournament)
        """delete self tournois after save"""
        self.tournois.clear()

    def run_report_players_alph(self):
        """reports"""
        rep.print_players_order_alphabetics(self)
    def run_report_players_classment(self):
        rep.print_players_order_classment(self)

    def run_report_tournament(self):
        rep.print_all_tournaments(self)
