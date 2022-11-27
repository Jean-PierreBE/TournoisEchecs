"""Create tournament view"""
from ProjectTournoi.controllers.tools import check_date, check_classment, check_sex
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
        while check == False:
            date_entry = input(vr.MESSAGE_ENCODE_BIRTHDATE)
            if not date_entry:
                return birthdate_in
            check = check_date(date_entry)
            if check == True:
                return date_entry

    def prompt_for_sex(self, codesex_in):
        """Prompt for a code sex"""
        check = False
        while check == False:
            codesex = input(vr.MESSAGE_ENCODE_SEX)
            if not codesex:
                return codesex_in
            check = check_sex(codesex.upper())
            if check == True:
                return codesex.upper()

    def prompt_for_classment(self, classment_in):
        """Prompt for a classment"""
        check = False
        while check == False:
            classment = input(vr.MESSAGE_ENCODE_CLASSMENT)
            if not classment:
                return classment_in
            check = check_classment(classment)
            if check == True:
                return classment

    def prompt_for_continue_players(self):
        """Prompt to continue encode players"""
        response = input(vr.MESSAGE_CONTINUE_ENCODE_PLAYERS)
        if not response:
            return 'None'
        return response.upper()

    def prompt_choose_indice_players(self, num_player):
        """Prompt to continue encode players"""
        if num_player == -1:
            question = vr.MESSAGE_SELECT_INDICE_PLAYER
        else:
            question = vr.MESSAGE_SELECT_INDICE_PLAYER + str(num_player) + " : "
        response = input(question)
        if not response:
            return 1
        return int(response)


