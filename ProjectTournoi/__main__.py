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


def option1():
    print('Handle option \'Option 1\'')


def option2():
    tournoi.run()


def option3():
    print('Handle option \'Option 3\'')


def option4():
    print('Handle option \'Option 3\'')


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
       option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5:
        print("Au revoir et à bientôt !")
        exit()
    else:
        print('veuillez entrer un chiffre entre 1 et 4.')
