import datetime as dt
import ProjectTournoi.variables as vr

def get_result_player(list, element):
    for ind in range(len(list)):
        if list[ind].player_id == element:
            return ind
    return -1

"""check validity of the date"""
def check_date(date_entry):
    """check validity of the date DD/MM/YYYY"""
    if date_entry.find('/',2) != 2 or date_entry.find('/',5) != 5:
        print(vr.MESSAGE_WRONG_DATE_FORMAT)
        return False
    else:
        try:
            date_check = int(date_entry.replace('/',''))
        except ValueError:
            print(vr.MESSAGE_NOT_NUMERIC)
            return False
        day, month, year = map(int, date_entry.split('/'))
        try:
            date_check = dt.date(int(year), int(month), int(day))
        except ValueError:
            print(vr.MESSAGE_WRONG_DATE_INVALID)
            return False
        return True

def check_time(time_entry):
    """check validity of the time HH:MM"""
    if time_entry.find(':',2) != 2:
        print(vr.MESSAGE_WRONG_TIME_FORMAT)
        return False
    else:
        try:
            time_check = int(time_entry.replace(':',''))
        except ValueError:
            print(vr.MESSAGE_NOT_NUMERIC)
            return False
        time, minute = map(int, time_entry.split(':'))
        try:
            time_check = dt.time(time, minute)
        except ValueError:
            print(vr.MESSAGE_WRONG_TIME_INVALID)
            return False
        return True

def check_classment(classment_entry):
    """check validity of the classment"""
    try:
        classment_check = int(classment_entry)
    except ValueError:
        print(vr.MESSAGE_NOT_NUMERIC)
        return False
    if classment_check < vr.CLASSMENT_MIN:
        print(vr.MESSAGE_CLASSMENT_MIN)
        return False
    elif(classment_check > vr.CLASSMENT_MAX):
        print(vr.MESSAGE_CLASSMENT_MAX)
        return False
    else:
        return True

def check_sex(sex_entry):
    """check validity of sex"""
    if sex_entry in vr.CODE_SEXE:
        return True
    else:
        print(vr.MESSAGE_WRONG_SEX)
        return False

def check_answer_y_n(answer_entry):
    """check validity of the classment"""
    if answer_entry != vr.ANSWER_NO and answer_entry != vr.ANSWER_YES:
        print(vr.MESSAGE_BAD_ANSWER_Y_OR_N)
        return False
    else:
        return True

def check_result(result_entry):
    """check validity of the result"""
    try:
        result_check = int(result_entry)
    except ValueError:
        print(vr.MESSAGE_NOT_NUMERIC)
        return False
    if result_check in vr.RESULTS:
        return True
    else:
        print(vr.MESSAGE_WRONG_RESULT)
        return False

def check_game(game_entry):
    """check validity of the game"""
    try:
        game_check = int(game_entry)
    except ValueError:
        print(vr.MESSAGE_NOT_NUMERIC)
        return False
    if game_check in vr.GAMES:
        return True
    else:
        print(vr.MESSAGE_WRONG_GAME)
        return False

def check_indice(indice_entry, indice_max):
    """check validity of indice"""
    try:
        indice_check = int(indice_entry)
    except ValueError:
        print(vr.MESSAGE_NOT_NUMERIC)
        return False
    if indice_check > indice_max or indice_check < 1:
        print(vr.MESSAGE_PLAYER_OUT_OF_RANGE)
        return False
    else:
        return True

def check_round_restart(round_entry, round_max):
    """check validity of round to restart"""
    try:
        round_check = int(round_entry)
    except ValueError:
        print(vr.MESSAGE_NOT_NUMERIC)
        return False
    if (round_check > round_max) or (round_check > vr.NUMBER_ROUNDS) or (round_check) < 1:
        print(vr.MESSAGE_ROUND_OUT_OF_RANGE)
        return False
    else:
        return True

"""Search if player 1 and player 2 played already """
def search_couple1(list, element_a, element_b):
    for indr in range(len(list)):
        for indg in range(len(list[indr].games)):
            if list[indr].games[indg].player_a == element_a and list[indr].games[indg].player_b == element_b:
                return True
            if list[indr].games[indg].player_b == element_a and list[indr].games[indg].player_a == element_b:
                return True
    return False
