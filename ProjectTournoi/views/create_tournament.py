"""management of views"""
import datetime as dt
import ProjectTournoi.tools.constants as vr
from ProjectTournoi.tools.check import check_answer_y_n, check_date, check_indice, check_round_restart, check_name


class CreateTournament:

    def prompt_for_area(self):
        """prompt for the area of tournament"""
        check = False
        while check is False:
            area = input(vr.MESSAGE_ENCODE_AREA)
            check = check_name(area)
            if check is True:
                return area

    def prompt_for_date(self):
        """prompt for the date of tournament"""
        check = False
        while check is False:
            date_entry = input(vr.MESSAGE_ENCODE_DATE_TOURNAMENT)
            if not date_entry:
                return dt.date.today().strftime("%d/%m/%Y")
            check = check_date(date_entry)
            if check is True:
                return date_entry

    def prompt_for_description(self):
        """prompt for the description of tournament"""
        check = False
        while check is False:
            description = input(vr.MESSAGE_ENCODE_DESCRIPTION)
            check = check_name(description)
            if check is True:
                return description

    def prompt_for_continue_tournament(self):
        """Prompt for a score"""
        check = False
        while check is False:
            response = input(vr.MESSAGE_CONTINUE_ENCODE_TOURNAMENT)
            check = check_answer_y_n(response.upper())
            if check is True:
                return response.upper()

    def prompt_continue_another_tournament(self):
        """Prompt for update another tournament"""
        check = False
        while check is False:
            response = input(vr.MESSAGE_CONTINUE_ANOTHER_TOURNAMENT)
            check = check_answer_y_n(response.upper())
            if check is True:
                return response.upper()

    def prompt_choose_tournament(self, number_tournament_available):
        check = False
        while check is False:
            response = input(vr.MESSAGE_SELECT_INDICE_TOURNAMENT)
            check = check_indice(response, number_tournament_available)
            if check is True:
                return int(response)

    def prompt_choose_round_deb(self, number_round_available):
        check = False
        while check is False:
            response = input(vr.MESSAGE_SELECT_ROUND_RESTART)
            check = check_round_restart(response, number_round_available)
            if check is True:
                return int(response)

    def prompt_list_tournaments_empty(self):
        """list empty"""
        print(vr.MESSAGE_LIST_TOURNAMENTS_EMPTY)
