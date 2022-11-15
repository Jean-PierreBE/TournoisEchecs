from prettytable import PrettyTable
import ProjectTournoi.controllers.tools as tl
import ProjectTournoi.variables as vr

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

    def list_results_tournaments(self, status, area, date, players):
        """Create list of all players"""
        table = PrettyTable()
        lib_status = 'définitif'
        if status == 0:
            lib_status = 'provisoire'
        table.title = 'Résultat ' + lib_status + ' du tournoi du ' + str(date) + ' à ' + area
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
                lib_result = 'Pas de résultat'
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

    def list_turning_round(self, tournoi, num_round, games):
        """Create list of results by round"""
        table = PrettyTable()

        table.title = 'Déroulement du round n° ' + str(num_round + 1) + ' du Tournoi du ' + str(tournoi.date) + ' à ' + tournoi.area
        table.field_names = ['Game', 'Id Joueur A', 'Joueur A','Id Joueur B', 'Joueur B', 'Résultat']
        imin = vr.NUMBER_GAMES * (num_round)
        imax = vr.NUMBER_GAMES * (num_round + 1)
        for indg in range(imin, imax):
            ind_a = tl.get_result_player(tournoi.players, games[indg].player_A)
            ind_b = tl.get_result_player(tournoi.players, games[indg].player_B)
            lib_result = 'En attente'
            if games[indg].result == 0:
                lib_result = 'Match nul'
            if games[indg].result == 1:
                lib_result = 'Joueur A vainqueur'
            if games[indg].result == 2:
                lib_result = 'Joueur B vainqueur'
            table.add_row([games[indg].game_id,
                           games[indg].player_A,
                           tournoi.players[ind_a].lastname + ' ' + tournoi.players[ind_a].firstname,
                           games[indg].player_B,
                           tournoi.players[ind_b].lastname + ' ' + tournoi.players[ind_b].firstname,
                           lib_result])
        print(table)