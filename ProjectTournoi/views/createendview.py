from prettytable import PrettyTable
import ProjectTournoi.controllers.tools as tl

class CreateEndView:

    def list_players(self, area, date, players):
        """Create list of all players"""
        table = PrettyTable()

        table.title = 'Liste des joueurs du tournoi du ' + str(date) + ' à ' + area
        table.field_names = ['Nom', 'Prénom', 'Date de naissance', 'sexe', 'classement']
        for iplayer in range(len(players)):
            table.add_row([players[iplayer].lastname, players[iplayer].firstname, players[iplayer].birthdate, players[iplayer].sex, players[iplayer].classment])

        print(table)

    def list_tournaments(self, area, date, description):
        """Create list of all players"""
        table = PrettyTable()
        table.title = 'liste des Tournois'
        table.field_names = ['Lieu', 'date', 'Description']
        table.add_row([area, date, description])

        print(table)

    def list_results_tournaments(self, area, date, players):
        """Create list of all players"""
        table = PrettyTable()
        table.title = 'Résultat du tournoi du ' + str(date) + ' à ' + area
        table.field_names = ['Nom', 'Prénom', 'Score']
        for iplayer in range(len(players)):
            table.add_row([players[iplayer].lastname, players[iplayer].firstname, players[iplayer].score])

        print(table)

    def list_results_rounds(self, tournoi):
        """Create list of results by round"""
        table = PrettyTable()

        table.title = 'Résultats du Tournoi du ' + str(tournoi.date) + ' à ' + tournoi.area + ' par round'
        table.field_names = ['round', 'Game', 'Joueur A', 'Joueur B','Résultat']
        for indr in range(len(tournoi.rounds)):
            for indg in range(len(tournoi.rounds[indr].games)):
                ind_a = tl.get_result_player(tournoi.players, tournoi.rounds[indr].games[indg].player_A)
                ind_b = tl.get_result_player(tournoi.players, tournoi.rounds[indr].games[indg].player_B)
                if tournoi.rounds[indr].games[indg].result == 0:
                   lib_result = 'Match nul'
                if tournoi.rounds[indr].games[indg].result == 1:
                    lib_result = 'Joueur A vainqueur'
                if tournoi.rounds[indr].games[indg].result == 2:
                    lib_result = 'Joueur B vainqueur'
                table.add_row([tournoi.rounds[indr].round_id,
                               tournoi.rounds[indr].games[indg].game_id,
                               tournoi.players[ind_a].lastname + ' ' + tournoi.players[ind_a].firstname,
                               tournoi.players[ind_b].lastname + ' ' + tournoi.players[ind_b].firstname,
                               lib_result])
        print(table)