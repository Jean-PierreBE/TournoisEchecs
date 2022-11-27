from ProjectTournoi.models import player as pl
from ProjectTournoi.models import tournament as tn
from ProjectTournoi.db import db_players, db_tournament

import datetime as dt
from ProjectTournoi.variables import MESSAGE_WRONG_DATE_FORMAT, MESSAGE_WRONG_DATE_INVALID, MESSAGE_NOT_NUMERIC,\
                                    MESSAGE_CLASSMENT_MIN, MESSAGE_CLASSMENT_MAX, CLASSMENT_MIN, CLASSMENT_MAX,\
                                    SEX_MALE, SEX_FEMALE, MESSAGE_WRONG_SEX
def get_result_player(list, element):
    for ind in range(len(list)):
        if list[ind].player_id == element:
            return ind
    return -1

"""Search if player 1 and player 2 played already """

"""check validity of the date"""
def check_date(date_entry):
    """check validity of the date DD/MM/YYYY"""
    if date_entry.find('/',2) != 2 or date_entry.find('/',5) != 5:
        print(MESSAGE_WRONG_DATE_FORMAT)
        return False
    else:
        try:
            date_check = int(date_entry.replace('/',''))
        except ValueError:
            print(MESSAGE_NOT_NUMERIC)
            return False
        day, month, year = map(int, date_entry.split('/'))
        try:
            date_check = dt.date(int(year), int(month), int(day))
        except ValueError:
            print(MESSAGE_WRONG_DATE_INVALID)
            return False
        return True

def check_classment(classment_entry):
    """check validity of the classment"""
    try:
        classment_check = int(classment_entry)
    except ValueError:
        print(MESSAGE_NOT_NUMERIC)
        return False
    if classment_check < CLASSMENT_MIN:
        print(MESSAGE_CLASSMENT_MIN)
        return False
    elif(classment_check > CLASSMENT_MAX):
        print(MESSAGE_CLASSMENT_MAX)
        return False
    else:
        return True

def check_sex(sex_entry):
    """check validity of the classment"""
    if sex_entry != SEX_MALE and sex_entry != SEX_FEMALE:
        print(MESSAGE_WRONG_SEX)
        return False
    else:
        return True

def search_couple(list, element_a, element_b):
    for indr in range(len(list)):
        for indg in range(len(list[indr].games)):
            if list[indr].games[indg].player_a == element_a and list[indr].games[indg].player_b == element_b:
                return True
            if list[indr].games[indg].player_b == element_a and list[indr].games[indg].player_a == element_b:
                return True
    return False

def download_players():
    players = []
    for row in db_players:
        player = pl.Player(row['player_id'], row['lastname'], row['firstname'], row['birthdate'], row['sex'],
                           row['classment'])
        players.append(player)
    return players

def download_tournaments():
    tournaments = []
    for row in db_tournament:
        tournament = tn.Tournament(row['tournament_id'], row['area'], row['date'], row['description'],'','')
        tournaments.append(tournament)
    return tournaments