"""Create round view"""
import datetime as dt
import ProjectTournoi.variables as vr

class CreateRound:

    def prompt_for_begin_date(self,num_round):
        """Prompt for a begin date"""
        date_entry = input("Entrez la date de début du round n° " + str(num_round + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.DATE_BEGIN[num_round]
        day, month, year = map(int, date_entry.split('/'))
        begin_date = dt.date(year, month, day)
        return begin_date

    def prompt_for_begin_time(self,num_round):
        """Prompt for a time date"""
        time_entry = input("Entrez l'heure de début du round n° " + str(num_round + 1) + " au format HH:MM : ")
        if not time_entry:
            time_entry = vr.TIME_BEGIN[num_round]
        hour,minute = map(int, time_entry.split(':'))
        begin_time = dt.time(hour,minute)
        return begin_time

    def prompt_for_end_date(self,num_round):
        """Prompt for a end date"""
        date_entry = input("Entrez la date de fin du round n° " + str(num_round + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = vr.DATE_END[num_round]
        day, month, year = map(int, date_entry.split('/'))
        end_date = dt.date(year, month, day)
        return end_date

    def prompt_for_end_time(self,num_round):
        """Prompt for a time date"""
        time_entry = input("Entrez l'heure de fin du round n° " + str(num_round + 1) + " au format HH:MM : ")
        if not time_entry:
            time_entry = vr.TIME_END[num_round]
        hour,minute = map(int, time_entry.split(':'))
        end_time = dt.time(hour,minute)
        return end_time