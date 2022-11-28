"""Create tournament view"""
import datetime as dt
import ProjectTournoi.variables as vr
from ProjectTournoi.controllers.tools import check_answer_y_n, check_date
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
        while check == False:
            date_entry = input(vr.MESSAGE_ENCODE_DATE_TOURNAMENT)
            if not date_entry:
                return  dt.date.today().strftime("%d/%m/%Y")
            check = check_date(date_entry)
            if check == True:
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
        while check == False:
            response = input(vr.MESSAGE_CONTINUE_ENCODE_TOURNAMENT)
            if not response:
                return vr.ANSWER_NO
            check = check_answer_y_n(response.upper())
            if check == True:
                return response.upper()

    def prompt_continue_another_tournament(self):
        """Prompt for update another tournament"""
        check = False
        while check == False:
            response = input(vr.MESSAGE_CONTINUE_ANOTHER_TOURNAMENT)
            if not response:
                return vr.ANSWER_NO
            check = check_answer_y_n(response.upper())
            if check == True:
                return response.upper()

