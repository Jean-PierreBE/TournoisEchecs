"""Variables"""
NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_GAMES = 4
ID_PLAYER = 'Player_'
ID_TOURNAMENT = 'Tour_'
ID_ROUND = 'Round_'
ID_GAME = 'Game_'
ANSWER_YES = 'Y'
ANSWER_NO = 'N'
MESSAGE_BAD_ANSWER_Y_OR_N = "Veuillez encoder 'Y' ou 'N' !"
MESSAGE_BAD_ANSWER_1_OR_2 = "Veuillez encoder 1 ou 2 !"
MESSAGE_PLAYER_OUT_OF_RANGE = "Veuillez selectionner un indice dans la list !"
MESSAGE_PLAYER_ALLREADY_SELECTED = "Joueur déja selectionné !"
MESSAGE_WRONG_GAME = "Veuillez encoder 1 ,2 ,3 ou 4 !"
MESSAGE_WRONG_RESULT = "Veuillez encoder 0, 1 ou 2 !"
TOURNAMENT_STATUS = {'new' : 0, 'Active' : 1, 'closed' : 2}
INVITE_CHOOSE_8_PLAYERS = "Veuillez choisir 8 joueurs en selectionnant l'indice "

"""menu"""
menu_options = {
    1: 'Encodage nouveaux joueurs',
    2: 'Mise à jour joueurs ',
    3: 'Encodage nouveau tournoi ',
    4: 'Mise à jour tournoi',
    5: 'Liste des joueurs par ordre alphabétique',
    6: 'Liste des joueurs par classement ',
    7: 'Liste de tous les tournois',
    8: 'Exit',
}


"""Constants for tournament"""
AREA_DEFAULT = "A completer"
DESCRIPTION_DEFAULT = "A completer"
"""Constants for players"""
LAST_NAME_DEFAULT = 'A completer'
FIRST_NAME_DEFAULT = 'A completer'
BIRTHDATE_DEFAULT = '01/01/1900'
SEX_DEFAULT = 'A completer'
CLASSMENT_DEFAULT = 400
