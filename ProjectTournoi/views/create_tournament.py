"""Create tournament view"""
import datetime as dt
import ProjectTournoi.tools.constants as vr
from ProjectTournoi.tools.check import check_answer_y_n, check_date, check_indice, check_round_restart


class CreateTournament:

    def prompt_for_area(self):
        """prompt for the area of tournament"""
        area = input(vr.MESSAGE_ENCODE_AREA)
        if not area:
            return vr.AREA_DEFAULT
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
        description = input(vr.MESSAGE_ENCODE_DESCRIPTION)
        if not description:
            return vr.DESCRIPTION_DEFAULT
        return description

    def prompt_for_continue_tournament(self):
        """Prompt for a score"""
        check = False
        while check is False:
            response = input(vr.MESSAGE_CONTINUE_ENCODE_TOURNAMENT)
            if not response:
                return vr.ANSWER_NO
            check = check_answer_y_n(response.upper())
            if check is True:
                return response.upper()

    def prompt_continue_another_tournament(self):
        """Prompt for update another tournament"""
        check = False
        while check is False:
            response = input(vr.MESSAGE_CONTINUE_ANOTHER_TOURNAMENT)
            if not response:
                return vr.ANSWER_NO
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
