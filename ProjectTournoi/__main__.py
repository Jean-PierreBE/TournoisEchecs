"""Entry point"""
from ProjectTournoi.controllers.base import Controller
import ProjectTournoi.views.createtournament as vt
import ProjectTournoi.views.createplayer as vp
import ProjectTournoi.views.createround as vr
import ProjectTournoi.views.creategame as vg
import ProjectTournoi.views.createendview as vv
from ProjectTournoi.variables import menu_options, MESSAGE_NOT_NUMERIC, TITLE_MENU, \
                MESSAGE_INVITE_MENU, MESSAGE_GOOD_BYE, MESSAGE_SELECT_MENU


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
    option = ''
    try:
        option = int(input(MESSAGE_INVITE_MENU))
    except ValueError:
        print(MESSAGE_NOT_NUMERIC)
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
        print(MESSAGE_GOOD_BYE)
        exit()
    else:
        print(MESSAGE_SELECT_MENU)
