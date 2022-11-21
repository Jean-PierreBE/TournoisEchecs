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
    1: 'Créations de joueurs',
    2: 'Mise à jour joueurs ',
    3: 'Encodage nouveau tournoi ',
    4: 'Liste des joueurs par ordre alphabétique',
    5: 'Liste des joueurs par classement ',
    6: 'Liste de tous les tournois',
    7: 'Exit',
}


"""DataBase"""
DB_TOURNAMENT = 'db_Tournament.json'
DB_PLAYERS = 'db_Players.json'
TABLE_TOURNAMENT = 'tournament'
PLAYERS_TOURNAMENT = 'players'


"""Constants for tournament"""
AREA = "Bruxelles"
DESCRIPTION = "Tournoi d'echecs avec 4 tours , 4 parties pour chaque tour et 8 joueurs"
"""Constants for players"""
LAST_NAME = ['STEIN','STEINER','STEINMANN','STEINMEYER','STERLING','STERMANN','STERMEYER','MEYER']
FIRST_NAME = ['Jean-Pierre','Jeanne','Jean','Paula','Patrick','Lola','Paul','Helene']
BIRTHDATE = ['10/03/1965','11/04/1966','12/05/1967','13/06/1968','14/07/1969','15/08/1970','16/09/1971','17/10/1972']
SEX = ['M','F','M','F','M','F','M','F']
CLASSMENT = [1300,600,1000,1200,900,1250,800,2050]
