"""Create round view"""
import datetime as dt
import time as tm
from ProjectTournoi.controllers.tools import check_date, check_time
import ProjectTournoi.variables as vr


class CreateRound:

    def prompt_for_begin_date(self, num_round):
        """Prompt for a begin date"""
        check = False
        while check is False:
            date_entry = input(vr.MESSAGE_BEGIN_DATE_ROUND.format(num_round + 1))
            if not date_entry:
                return dt.date.today().strftime("%d/%m/%Y")
            check = check_date(date_entry)
            if check is True:
                return date_entry

    def prompt_for_begin_time(self, num_round):
        """Prompt for a time date"""
        check = False
        while check is False:
            time_entry = input(vr.MESSAGE_BEGIN_TIME_ROUND.format(num_round + 1))
            if not time_entry:
                return tm.strftime("%H:%M:%S", tm.localtime())
            check = check_time(time_entry)
            if check is True:
                return time_entry

    def prompt_for_end_date(self, num_round):
        """Prompt for a end date"""
        check = False
        while check is False:
            date_entry = input(vr.MESSAGE_END_DATE_ROUND.format(num_round + 1))
            if not date_entry:
                return dt.date.today().strftime("%d/%m/%Y")
            check = check_date(date_entry)
            if check is True:
                return date_entry

    def prompt_for_end_time(self, num_round):
        """Prompt for a time date"""
        check = False
        while check is False:
            time_entry = input(vr.MESSAGE_END_TIME_ROUND.format(num_round + 1))
            if not time_entry:
                return tm.strftime("%H:%M:%S", tm.localtime())
            check = check_time(time_entry)
            if check is True:
                return time_entry
