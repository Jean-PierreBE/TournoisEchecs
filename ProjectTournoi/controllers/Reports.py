import ProjectTournoi.views.createendview as cv

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