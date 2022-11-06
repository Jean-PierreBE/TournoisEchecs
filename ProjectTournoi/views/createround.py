"""Create round view"""
import datetime as dt
import ProjectTournoi.variables as vr

class CreateRound:

    def prompt_for_begin_date(self,i):
        """Prompt for a begin date"""
        date_entry = input("Entrez la date de début du round n° " + str(i + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.DATE_BEGIN[i]
        day, month, year = map(int, date_entry.split('/'))
        begin_date = dt.date(year, month, day)
        return begin_date

    def prompt_for_end_date(self,i):
        """Prompt for a end date"""
        date_entry = input("Entrez la date de fin du round n° " + str(i + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.DATE_END[i]
        day, month, year = map(int, date_entry.split('/'))
        end_date = dt.date(year, month, day)
        return end_date