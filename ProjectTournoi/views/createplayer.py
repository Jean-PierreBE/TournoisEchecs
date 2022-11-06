"""Create tournament view"""
import datetime as dt
import ProjectTournoi.variables as vr

class CreatePlayer:
    def prompt_for_lastname(self,i):
        """Prompt for a last name."""
        lastname = input("tapez le nom du joueur n° " + str(i+1) + " : ")
        if not lastname:
            return vr.LAST_NAME[i]
        return lastname

    def prompt_for_firstname(self,i):
        """Prompt for a first name."""
        firstname = input("tapez le prénom du joueur n° " + str(i+1) + " : ")
        if not firstname:
            return vr.FIRST_NAME[i]
        return firstname

    def prompt_for_birthdate(self,i):
        """Prompt for a birthdate"""
        date_entry = input("Entrez la date de naissance du joueur n° " + str(i+1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.BIRTHDATE[i]
        day, month, year = map(int, date_entry.split('/'))
        birthdate = dt.date(year, month, day)
        return birthdate

    def prompt_for_sex(self,i):
        """Prompt for a code sex"""
        codesex = input("Entrez le genre du joueur n° " + str(i+1) + " (M/F/Not Defined) : ")
        if not codesex:
            return vr.SEX[i]
        return codesex

    def prompt_for_classment(self,i):
        """Prompt for a classment"""
        classment = input("Entrez le dernier classement du joueur n° " + str(i+1) + ": ")
        if not classment:
            return vr.CLASSMENT[i]
        return classment