"""Entry point"""
from ProjectTournoi.controllers.base import Controller
import ProjectTournoi.views.createtournament as vt
import ProjectTournoi.views.createplayer as vp
import ProjectTournoi.views.createround as vr
import ProjectTournoi.views.creategame as vg
import ProjectTournoi.views.createendview as vv
from ProjectTournoi.variables import menu_options

def print_menu():

    print("Gestion de tournois d'échecs")
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
        option = int(input('Entrez votre choix: '))
    except:
        print('caractères non numériques ...')
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
        print("Au revoir et à bientôt !")
        exit()
    else:
        print('veuillez entrer un chiffre entre 1 et 7.')
