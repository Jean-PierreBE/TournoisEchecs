"""Create round view"""
import datetime as dt
import time as tm

class CreateRound:

    def prompt_for_begin_date(self,num_round):
        """Prompt for a begin date"""
        date_entry = input("Entrez la date de début du round n° " + str(num_round + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = dt.date.today().strftime("%d/%m/%Y")
        return date_entry

    def prompt_for_begin_time(self,num_round):
        """Prompt for a time date"""
        time_entry = input("Entrez l'heure de début du round n° " + str(num_round + 1) + " au format HH:MM : ")
        if not time_entry:
            time_entry = tm.strftime("%H:%M:%S", tm.localtime())
        return time_entry

    def prompt_for_end_date(self,num_round):
        """Prompt for a end date"""
        date_entry = input("Entrez la date de fin du round n° " + str(num_round + 1) + " au format DD/MM/YYYY : ")
        if not date_entry:
            date_entry = dt.date.today().strftime("%d/%m/%Y")
        return date_entry

    def prompt_for_end_time(self,num_round):
        """Prompt for a time date"""
        time_entry = input("Entrez l'heure de fin du round n° " + str(num_round + 1) + " au format HH:MM : ")
        if not time_entry:
            time_entry = tm.strftime("%H:%M:%S", tm.localtime())
        return time_entry