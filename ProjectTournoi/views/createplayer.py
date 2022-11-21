"""Create tournament view"""
import datetime as dt
import ProjectTournoi.variables as vr

class CreatePlayer:
    def prompt_for_lastname(self,num_player):
        """Prompt for a last name."""
        if num_player + 1 > 0:
            question = "tapez le nom du joueur n° " + str(num_player + 1) + " : "
        else:
            question = "tapez le nom du joueur : "
        lastname = input(question)
        if not lastname:
            return vr.LAST_NAME[num_player]
        return lastname.upper()

    def prompt_for_firstname(self,num_player):
        """Prompt for a first name."""
        if num_player + 1 > 0:
            question = "tapez le prénom du joueur n° " + str(num_player + 1) + " : "
        else:
            question = "tapez le prénom du joueur  : "
        firstname = input(question)
        if not firstname:
            return vr.FIRST_NAME[num_player]
        return firstname

    def prompt_for_birthdate(self,num_player):
        """Prompt for a birthdate"""
        if num_player + 1 > 0:
            question = "Entrez la date de naissance du joueur n° " + str(num_player + 1) + " au format DD/MM/YYYY : "
        else:
            question = "Entrez la date de naissance du joueur au format DD/MM/YYYY : "
        date_entry = input(question)
        if not date_entry:
            date_entry = vr.BIRTHDATE[num_player]
        day, month, year = map(int, date_entry.split('/'))
        birthdate = dt.date(year, month, day)
        return birthdate

    def prompt_for_sex(self,num_player):
        """Prompt for a code sex"""
        if num_player + 1 > 0:
            question = "Entrez le genre du joueur n° " + str(num_player + 1) + " (M/F) : "
        else:
            question = "Entrez le genre du joueur (M/F) : "
        codesex = input(question)
        if not codesex:
           return 'M'
        return codesex.upper()

    def prompt_for_classment(self,num_player):
        """Prompt for a classment"""
        if num_player + 1 > 0:
            question = "Entrez le dernier classement du joueur n° " + str(num_player + 1) + ": "
        else:
            question = "Entrez le dernier classement du joueur n° : "
        classment = input(question)
        try:
            return int(classment)
        except ValueError:
            return 400

    def prompt_for_continue_players(self):
        """Prompt to continue encode players"""
        response = input("Voulez-vous continuer à encoder des joueurs (Y/N) ? ")
        if not response:
            return 'None'
        return response.upper()

    def prompt_for_choose_players(self):
        """Prompt to continue encode players"""
        response = input("Voulez-vous encoder des joueurs (1) ou les sélectionner à partir d'une liste (2) ? ")
        if not response:
            return 2
        return int(response)

    def prompt_choose_indice_players(self, num_player):
        """Prompt to continue encode players"""
        response = input("Selectionner un indice pour le joueur " + str(num_player) + " : ")
        if not response:
            return 1
        return int(response)
