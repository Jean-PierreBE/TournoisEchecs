"""controller for reports"""
import ProjectTournoi.views.create_end_view as cv
import ProjectTournoi.controllers.acces_db as db
from ProjectTournoi.tools.constants import TITLE_PLAYERS_ALPH, TITLE_PLAYERS_CLASS


class Controller_reports:

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
        cv.CreateEndView.list_results_tournaments(self, 1, tournoi.date, tournoi.players)

    def print_players_order_alphabetics(self):
        players = db.controller_db.download_players(self)
        sorted_player = sorted(players, key=lambda e: (e.lastname, e.firstname))
        cv.CreateEndView.list_players_sort(self, sorted_player, TITLE_PLAYERS_ALPH)

    def print_players_order_classment(self):
        players = db.controller_db.download_players(self)
        sorted_player = sorted(players, key=lambda e: e.classment)
        cv.CreateEndView.list_players_sort(self, sorted_player, TITLE_PLAYERS_CLASS)

    def print_all_tournaments(self):
        tournaments = db.controller_db.download_tournaments(self)
        sorted_tournaments = sorted(tournaments, key=lambda e: e.date)
        cv.CreateEndView.list_tournaments_all(self, sorted_tournaments)
