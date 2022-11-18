"""Variables"""
NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 1
NUMBER_GAMES = 4
ID_PLAYER = 'Player_'
ID_TOURNAMENT = 'Tour_'
ID_ROUND = 'Round_'
ID_GAME = 'Game_'
ANSWER_YES = 'Y'
ANSWER_NO = 'N'
MESSAGE_BAD_ANSWER = "Veuillez encoder 'Y' ou 'N' !"
MESSAGE_WRONG_GAME = "Veuillez encoder 1 ,2 ,3 ou 4 !"
MESSAGE_WRONG_RESULT = "Veuillez encoder 0, 1 ou 2 !"
TOURNAMENT_STATUS = {'new' : 0, 'Active' : 1, 'closed' : 2}

"""menu"""
menu_options = {
    1: 'Créations de joueurs',
    2: 'Encodage nouveau tournoi ',
    3: 'Reprise tournois existants',
    4: 'Rapports',
    5: 'Exit',
}

"""DataBase"""
DB_TOURNAMENT = 'db_Tournament.json'
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
