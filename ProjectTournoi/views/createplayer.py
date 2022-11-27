"""Create tournament view"""
import datetime as dt
from ProjectTournoi.variables import LAST_NAME_DEFAULT,FIRST_NAME_DEFAULT, BIRTHDATE_DEFAULT, SEX_DEFAULT, CLASSMENT_DEFAULT
from ProjectTournoi.controllers.tools import check_date

class CreatePlayer:
    def prompt_for_lastname(self):
        """Prompt for a last name."""
        question = "tapez le nom du joueur : "
        lastname = input(question)
        if not lastname:
            return LAST_NAME_DEFAULT
        return lastname.upper()

    def prompt_for_firstname(self):
        """Prompt for a first name."""
        question = "tapez le prénom du joueur  : "
        firstname = input(question)
        if not firstname:
            return FIRST_NAME_DEFAULT
        return firstname

    def prompt_for_birthdate(self):
        """Prompt for a birthdate"""
        question = "Entrez la date de naissance du joueur au format DD/MM/YYYY : "
        date_entry = input(question)
        if not date_entry:
            date_entry = BIRTHDATE_DEFAULT
        response = False
        while response == False:
            response = check_date(date_entry)
            if response == True:
                return date_entry

    def prompt_for_sex(self):
        """Prompt for a code sex"""
        question = "Entrez le genre du joueur (M/F) : "
        codesex = input(question)
        if not codesex:
           return SEX_DEFAULT
        return codesex.upper()

    def prompt_for_classment(self):
        """Prompt for a classment"""
        question = "Entrez le dernier classement du joueur n° : "
        classment = input(question)
        try:
            return int(classment)
        except ValueError:
            return CLASSMENT_DEFAULT

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
        if num_player == -1:
            question = "Selectionner un indice pour le joueur "
        else:
            question = "Selectionner un indice pour le joueur " + str(num_player) + " : "
        response = input(question)
        if not response:
            return 1
        return int(response)

class UpdatePlayer:

    def prompt_for_lastname(self, lastname_in):
        """Prompt for a last name."""
        question = "tapez le nom du joueur : "
        lastname = input(question)
        if not lastname:
            return lastname_in
        return lastname.upper()

    def prompt_for_firstname(self, firstname_in):
        """Prompt for a first name."""
        question = "tapez le prénom du joueur  : "
        firstname = input(question)
        if not firstname:
            return firstname_in
        return firstname

    def prompt_for_birthdate(self, birthdate_in):
        """Prompt for a birthdate"""
        question = "Entrez la date de naissance du joueur au format DD/MM/YYYY : "
        date_entry = input(question)
        if not date_entry:
            date_entry = birthdate_in
        response = False
        while response == False:
            response = check_date(date_entry)
            if response == True:
                return date_entry

    def prompt_for_sex(self, codesex_in):
        """Prompt for a code sex"""
        question = "Entrez le genre du joueur (M/F) : "
        codesex = input(question)
        if not codesex:
           return codesex_in
        return codesex.upper()

    def prompt_for_classment(self, classment_in):
        """Prompt for a classment"""
        question = "Entrez le dernier classement du joueur n° : "
        classment = input(question)
        try:
            return int(classment)
        except ValueError:
            return classment_in
