"""Create tournament view"""
import datetime as dt
from ProjectTournoi.variables import AREA_DEFAULT, DESCRIPTION_DEFAULT
class CreateTournament:

    def prompt_for_area(self):
        """prompt for the area of tournament"""
        area = input("Entrez le lieu du tournoi : ")
        if not area:
            return AREA_DEFAULT
        return area

    def prompt_for_date(self):
        """prompt for the date of tournament"""
        date_entry = input("Entrez la date du tournoi au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = dt.date.today().strftime("%d/%m/%Y")
        return date_entry

    def prompt_for_description(self):
        """prompt for the description of tournament"""
        description = input("Entrez la description du tournoi : ")
        if not description:
            return DESCRIPTION_DEFAULT
        return description
