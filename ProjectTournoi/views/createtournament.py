"""Create tournament view"""
import datetime as dt
import ProjectTournoi.variables as vr
class CreateTournament:

    def prompt_for_area(self):
        """prompt for the area of tournament"""
        area = input("Entrez le lieu du tournoi : ")
        if not area:
            return vr.AREA
        return area

    def prompt_for_date(self):
        """prompt for the date of tournament"""
        date_entry = input("Entrez la date du tournoi au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.DATE_TOURNAMENT
        day,month,year  = map(int, date_entry.split('/'))
        date_tournament = dt.date(year, month, day)
        return date_tournament

    def prompt_for_description(self):
        """prompt for the description of tournament"""
        description = input("Entrez la description du tournoi : ")
        if not description:
            return vr.DESCRIPTION
        return description
