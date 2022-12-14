"""Beginning"""
from ProjectTournoi.controllers.base import Controller
import ProjectTournoi.views.create_tournament as vt
import ProjectTournoi.views.create_player as vp
import ProjectTournoi.views.create_round as vr
import ProjectTournoi.views.create_game as vg
import ProjectTournoi.views.create_end_view as vv
from ProjectTournoi.tools.constants import menu_options, TITLE_MENU, MESSAGE_INVITE_MENU, MESSAGE_GOOD_BYE
from ProjectTournoi.tools.check import check_menu


def prompt_for_menu():
    """Prompt for a score"""
    check = False
    while check is False:
        result = input(MESSAGE_INVITE_MENU)
        check = check_menu(result)
        if check is True:
            return int(result)


def print_menu():

    print(TITLE_MENU)
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


ctview = vt.CreateTournament()
cpview = vp.CreatePlayer()
crview = vr.CreateRound()
cgview = vg.CreateGame()
cvview = vv.CreateEndView()

tournoi = Controller(ctview, cpview, crview, cgview, cvview)


while True:
    print_menu()
    option = prompt_for_menu()
    if option == 1:
        tournoi.run_create_players()
    elif option == 2:
        tournoi.run_update_players()
    elif option == 3:
        tournoi.run_create_tournoi()
    elif option == 4:
        tournoi.run_update_tournoi()
    elif option == 5:
        tournoi.run_report_players_alph()
    elif option == 6:
        tournoi.run_report_players_classment()
    elif option == 7:
        tournoi.run_report_tournament()
    elif option == 8:
        tournoi.run_report_result_tournament()
    elif option == 9:
        print(MESSAGE_GOOD_BYE)
        exit()
