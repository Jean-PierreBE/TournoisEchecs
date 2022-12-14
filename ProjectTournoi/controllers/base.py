"""Define the main controller"""
import ProjectTournoi.controllers.reports as rep
import ProjectTournoi.controllers.tournament as ctn
import ProjectTournoi.controllers.round as rnd
import ProjectTournoi.controllers.player as ply

from ProjectTournoi.views import create_end_view as cv
from ProjectTournoi.views import create_player as cp
from ProjectTournoi.views import create_tournament as ct
from ProjectTournoi.tools.constants import NUMBER_ROUNDS, NUMBER_PLAYERS
import ProjectTournoi.controllers.acces_db as db

from ProjectTournoi.db import db_players, db_tournament


class Controller:
    """Main controller"""

    def __init__(self, ctview, cpview, crview, cgview, cvview):
        # models
        self.tournaments = []
        self.players = []
        self.current_tournament = ''
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
            ply.Controller_player.create_player(self, play_seq)
            encode_players = ply.Controller_player.get_players_continue(self)
        db.controller_db.insert_players(self, self.players)
        self.players.clear()

    def run_update_players(self):
        players = db.controller_db.download_players(self)
        if len(players) == 0:
            encode_players = False
            cp.CreatePlayer.prompt_list_players_empty(self)
        else:
            encode_players = True
            cv.CreateEndView.list_only_players(self, players)
            while encode_players:
                """Encode players"""
                num_play = cp.CreatePlayer.prompt_choose_indice_players(self, -1, len(players))
                player_out = ply.Controller_player.update_player(self, players[num_play-1])
                db.controller_db.update_player(self, player_out)
                encode_players = ply.Controller_player.get_players_continue(self)

    def run_update_tournoi(self):
        # list of tournaments
        self.tournaments = db.controller_db.download_tournaments(self)
        if len(self.tournaments) == 0:
            update_tournament = False
            ct.CreateTournament.prompt_list_tournaments_empty(self)
        else:
            update_tournament = True
            while update_tournament:
                cv.CreateEndView.list_only_tournaments(self, self.tournaments)
                """Choose tournament"""
                ind_tournament = ct.CreateTournament.prompt_choose_tournament(self, len(self.tournaments))
                tournament = self.tournaments[ind_tournament - 1]
                """check previous results"""
                cv.CreateEndView.list_results_rounds(self, tournament)
                """choose round to restart"""
                round_deb = ct.CreateTournament.prompt_choose_round_deb(self, len(tournament.rounds) + 1)
                """delete rounds if replayed"""
                for indc in range(round_deb - 1, len(tournament.rounds)):
                    del tournament.rounds[round_deb - 1]
                """update results tournament"""
                ply.Controller_player.update_score_if_replay(self, tournament)
                """execute tournament"""
                running_tournament = True
                while running_tournament:
                    for num_round in range(round_deb - 1, NUMBER_ROUNDS):
                        running_tournament = rnd.turning_round.turning_round(self, num_round, tournament)
                        if running_tournament is False:
                            break
                    """Affichage résultat tournoi"""
                    rep.Controller_reports.print_end_views(self, tournament)
                    """serialize object"""
                    db.controller_db.update_tournament(self, tournament)
                update_tournament = ctn.Controller_tournament.continue_another_tournament(self)

    def run_create_tournoi(self):
        """check if there's enough players"""
        if len(db_players) < NUMBER_PLAYERS:
            cp.CreatePlayer.prompt_list_not_enough_players(self, len(db_players))
        else:
            ctn.Controller_tournament.create_tournament(self, len(db_tournament))
            """choose players from a list"""
            ply.Controller_player.choose_players(self, self.current_tournament)
            """Rounds"""
            for num_round in range(NUMBER_ROUNDS):
                if rnd.turning_round.turning_round(self, num_round, self.current_tournament) is False:
                    break
            """Affichage résultat tournoi"""
            rep.Controller_reports.print_end_views(self, self.current_tournament)
            """insert tournament in db"""
            db.controller_db.insert_tournament(self, self.current_tournament)

    def run_report_players_alph(self):
        """reports"""
        rep.Controller_reports.print_players_order_alphabetics(self)

    def run_report_players_classment(self):
        rep.Controller_reports.print_players_order_classment(self)

    def run_report_tournament(self):
        rep.Controller_reports.print_all_tournaments(self)

    def run_report_result_tournament(self):
        # list of tournaments
        self.tournaments = db.controller_db.download_tournaments(self)
        if len(self.tournaments) == 0:
            consult_tournament = False
            ct.CreateTournament.prompt_list_tournaments_empty(self)
        else:
            consult_tournament = True
            while consult_tournament:
                cv.CreateEndView.list_only_tournaments(self, self.tournaments)
                """Choose tournament"""
                ind_tournament = ct.CreateTournament.prompt_choose_tournament(self, len(self.tournaments))
                tournament = self.tournaments[ind_tournament - 1]
                """Affichage résultat tournoi"""
                rep.Controller_reports.print_end_views(self, tournament)
                consult_tournament = ctn.Controller_tournament.continue_another_tournament(self)
