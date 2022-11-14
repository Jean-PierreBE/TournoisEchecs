"""Create tournament view"""
import datetime as dt
import ProjectTournoi.variables as vr

class CreatePlayer:
    def prompt_for_lastname(self,num_player):
        """Prompt for a last name."""
        lastname = input("tapez le nom du joueur n° " + str(num_player + 1) + " : ")
        if not lastname:
            return vr.LAST_NAME[num_player]
        return lastname

    def prompt_for_firstname(self,num_player):
        """Prompt for a first name."""
        firstname = input("tapez le prénom du joueur n° " + str(num_player + 1) + " : ")
        if not firstname:
            return vr.FIRST_NAME[num_player]
        return firstname

    def prompt_for_birthdate(self,num_player):
        """Prompt for a birthdate"""
        date_entry = input("Entrez la date de naissance du joueur n° " + str(num_player + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.BIRTHDATE[num_player]
        day, month, year = map(int, date_entry.split('/'))
        birthdate = dt.date(year, month, day)
        return birthdate

    def prompt_for_sex(self,num_player):
        """Prompt for a code sex"""
        codesex = input("Entrez le genre du joueur n° " + str(num_player + 1) + " (M/F) : ")
        if not codesex:
            return vr.SEX[num_player]
        return codesex

    def prompt_for_classment(self,num_player):
        """Prompt for a classment"""
        classment = input("Entrez le dernier classement du joueur n° " + str(num_player + 1) + ": ")
        if not classment:
            return vr.CLASSMENT[num_player]
        return classment