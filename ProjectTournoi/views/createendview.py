from prettytable import PrettyTable

class CreateEndView:

    def list_players(self, players):
        """Create list of all players"""
        table = PrettyTable()

        table.title = 'Liste des joueurs du tournoi'
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

    def list_rounds(self, tournoi):
        """Create list of all players"""
        table = PrettyTable()

        table.title = 'liste des Tournois'
        table.field_names = ['Lieu', 'date', 'Description']
        table.add_row(tournoi.area, tournoi.date, tournoi.description)

        print(table)