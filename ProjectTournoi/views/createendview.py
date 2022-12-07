from prettytable import PrettyTable
import ProjectTournoi.controllers.tools as tl
import ProjectTournoi.variables as vr


class CreateEndView:

    def list_players(self, area, date, players):
        """Create list of all players"""
        table = PrettyTable()

        table.title = 'Liste des joueurs du tournoi du ' + str(date) + ' à ' + area
        table.field_names = vr.COL_PLAYERS
        for iplayer in range(len(players)):
            table.add_row([players[iplayer].lastname, players[iplayer].firstname, players[iplayer].birthdate, players[iplayer].sex, players[iplayer].classment])

        print(table)

    def list_players_sort(self, players, title_rep):
        """Create list of all players"""
        table = PrettyTable()

        table.title = title_rep
        table.field_names = vr.COL_PLAYERS
        for iplayer in range(len(players)):
            table.add_row([players[iplayer].lastname, players[iplayer].firstname, players[iplayer].birthdate, players[iplayer].sex, players[iplayer].classment])

        print(table)

    def list_only_players(self, players):
        """Create list of all players"""
        table = PrettyTable()

        table.title = vr.TITLE_PLAYERS_DISPO
        table.field_names = vr.COL_PLAYERS_DISPO
        indp = 0
        for iplayer in range(len(players)):
            indp += 1
            table.add_row([indp, players[iplayer].player_id, players[iplayer].lastname, players[iplayer].firstname, players[iplayer].birthdate, players[iplayer].sex, players[iplayer].classment])

        print(table)

    def list_only_tournaments(self, tournaments):
        """Create list of all tournaments"""
        table = PrettyTable()
        table.title = vr.TITLE_TOURNAMENT_DISPO
        table.field_names = vr.COL_TOURNAMENT_DISPO
        indp = 0
        for itournament in range(len(tournaments)):
            indp += 1
            table.add_row([indp, tournaments[itournament].tournament_id, tournaments[itournament].area, tournaments[itournament].date, tournaments[itournament].description, len(tournaments[itournament].rounds)])

        print(table)

    def list_tournaments(self, area, date, description):
        """Create list of all players"""
        table = PrettyTable()
        table.title = vr.TITLE_TOURNAMENT_LIST
        table.field_names = vr.COL_TOURNAMENTS
        table.add_row([area, date, description])

        print(table)

    def list_tournaments_all(self, tournaments):
        """Create list of all players"""
        table = PrettyTable()
        table.title = vr.TITLE_TOURNAMENT_LIST
        table.field_names = vr.COL_TOURNAMENTS
        for itournoi in range(len(tournaments)):
            table.add_row([tournaments[itournoi].area, tournaments[itournoi].date, tournaments[itournoi].description])

        print(table)

    def list_results_tournaments(self, status, date, players):
        """Create list of all players"""
        table = PrettyTable()
        lib_status = vr.STATUS_TOURNAMENT[status]
        table.title = 'Résultats ' + lib_status + ' du tournoi du ' + str(date)
        table.field_names = ['Nom', 'Prénom', 'Score']
        for iplayer in range(len(players)):
            table.add_row([players[iplayer].lastname, players[iplayer].firstname, players[iplayer].score])

        print(table)

    def list_rounds(self, tournoi):
        """Create list of results by round"""
        table = PrettyTable()

        table.title = 'Rounds du Tournoi du ' + str(tournoi.date) + ' à ' + tournoi.area
        table.field_names = ['round', 'Date de début', 'Heure de début', 'Date de fin', 'Heure de fin']
        for indr in range(len(tournoi.rounds)):
            table.add_row([tournoi.rounds[indr].round_id, tournoi.rounds[indr].begindate,
                            tournoi.rounds[indr].begintime,
                            tournoi.rounds[indr].enddate,
                            tournoi.rounds[indr].endtime])
        print(table)

    def list_results_rounds(self, tournoi):
        """Create list of results by round"""
        table = PrettyTable()

        table.title = 'Résultats du Tournoi du ' + str(tournoi.date) + ' à ' + tournoi.area + ' par round'
        table.field_names = ['round', 'Game', 'Joueur A', 'Joueur B', 'Résultat']
        for indr in range(len(tournoi.rounds)):
            for indg in range(len(tournoi.rounds[indr].games)):
                ind_a = tl.get_result_player(tournoi.players, tournoi.rounds[indr].games[indg].player_a)
                ind_b = tl.get_result_player(tournoi.players, tournoi.rounds[indr].games[indg].player_b)
                if tournoi.rounds[indr].games[indg].result in vr.RESULTS:
                    lib_result = vr.GAME_RESULTS[tournoi.rounds[indr].games[indg].result]
                else:
                    lib_result = vr.NO_RESULT[0]
                table.add_row([tournoi.rounds[indr].round_id,
                               tournoi.rounds[indr].games[indg].game_id,
                               tournoi.players[ind_a].lastname + ' ' + tournoi.players[ind_a].firstname,
                               tournoi.players[ind_b].lastname + ' ' + tournoi.players[ind_b].firstname,
                               lib_result])
        print(table)

    def list_turning_round(self, num_round, tournoi):
        """Create list of results by round"""
        table = PrettyTable()
        table.title = vr.TITLE_TURNING_ROUND.format(str(num_round + 1), str(tournoi.date), tournoi.area)
        table.field_names = vr.COL_TURNING_ROUND
        for indg in range(vr.NUMBER_GAMES):
            ind_a = tl.get_result_player(tournoi.players, tournoi.rounds[num_round].games[indg].player_a)
            ind_b = tl.get_result_player(tournoi.players, tournoi.rounds[num_round].games[indg].player_b)
            if tournoi.rounds[num_round].games[indg].result in vr.RESULTS:
                lib_result = vr.GAME_RESULTS[tournoi.rounds[num_round].games[indg].result]
            else:
                lib_result = vr.NO_RESULT[1]
            table.add_row([tournoi.rounds[num_round].games[indg].game_id,
                           tournoi.rounds[num_round].games[indg].player_a,
                           tournoi.players[ind_a].lastname + ' ' + tournoi.players[ind_a].firstname,
                           tournoi.rounds[num_round].games[indg].player_b,
                           tournoi.players[ind_b].lastname + ' ' + tournoi.players[ind_b].firstname,
                           lib_result])
        print(table)
