import ProjectTournoi.views.createendview as cv
import ProjectTournoi.controllers.tools as tl

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
    cv.CreateEndView.list_results_tournaments(self,  1, tournoi.area, tournoi.date, tournoi.players)

def print_players_order_alphabetics(self):
    players = tl.download_players()
    sorted_player = sorted(players, key=lambda e: (e.lastname, e.firstname) )
    cv.CreateEndView.list_players_sort(self,sorted_player, "Liste des joueurs par ordre alphabetique")


def print_players_order_classment(self):
    players = tl.download_players()
    sorted_player = sorted(players, key=lambda e:e.classment )
    cv.CreateEndView.list_players_sort(self,sorted_player, "Liste des joueurs par classement")


def print_all_tournaments(self):
    tournaments = tl.download_tournaments()
    sorted_tournaments = sorted(tournaments, key=lambda e:e.date )
    cv.CreateEndView.list_tournaments1(self, sorted_tournaments)