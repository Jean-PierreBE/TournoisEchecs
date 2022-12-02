"""Create tournament view"""
from ProjectTournoi.controllers.tools import check_date, check_classment, check_sex, check_answer_y_n, check_indice
import ProjectTournoi.variables as vr
class CreatePlayer:

    def prompt_for_lastname(self, lastname_in):
        """Prompt for a last name."""
        lastname = input(vr.MESSAGE_ENCODE_LASTNAME)
        if not lastname:
            return lastname_in
        return lastname.upper()

    def prompt_for_firstname(self, firstname_in):
        """Prompt for a first name."""
        firstname = input(vr.MESSAGE_ENCODE_FIRSTNAME)
        if not firstname:
            return firstname_in
        return firstname

    def prompt_for_birthdate(self, birthdate_in):
        """Prompt for a birthdate"""
        check = False
        while check is False:
            date_entry = input(vr.MESSAGE_ENCODE_BIRTHDATE)
            if not date_entry:
                return birthdate_in
            check = check_date(date_entry)
            if check is True:
                return date_entry

    def prompt_for_sex(self, codesex_in):
        """Prompt for a code sex"""
        check = False
        while check is False:
            codesex = input(vr.MESSAGE_ENCODE_SEX)
            if not codesex:
                return codesex_in
            check = check_sex(codesex.upper())
            if check is True:
                return codesex.upper()

    def prompt_for_classment(self, classment_in):
        """Prompt for a classment"""
        check = False
        while check is False:
            classment = input(vr.MESSAGE_ENCODE_CLASSMENT)
            if not classment:
                return classment_in
            check = check_classment(classment)
            if check is True:
                return classment

    def prompt_for_continue_players(self):
        """Prompt to continue encode players"""
        check = False
        while check is False:
            response = input(vr.MESSAGE_CONTINUE_ENCODE_PLAYERS)
            check = check_answer_y_n(response.upper())
            if check is True:
                return response.upper()

    def prompt_choose_indice_players(self, num_player, indice_max):
        """Prompt to continue encode players"""
        if num_player == -1:
            question = vr.MESSAGE_SELECT_INDICE_PLAYER
        else:
            question = vr.MESSAGE_SELECT_INDICE_PLAYER + str(num_player) + " : "
        check = False
        while check is False:
            response = input(question)
            check = check_indice(response, indice_max)
            if check is True:
                return int(response)


