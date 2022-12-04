"""Constants"""
NUMBER_PLAYERS = 8
NUMBER_ROUNDS = 4
NUMBER_GAMES = 4
ID_PLAYER = 'Player_'
ID_TOURNAMENT = 'Tour_'
ID_ROUND = 'Round_'
ID_GAME = 'Game_'
ANSWER_YES = 'Y'
ANSWER_NO = 'N'
TOURNAMENT_STATUS = {'new': 0, 'Active': 1, 'closed': 2}
"""messages"""
MESSAGE_PLAYER_OUT_OF_RANGE = "Veuillez selectionner un indice dans la liste !"
MESSAGE_ROUND_OUT_OF_RANGE = "Veuillez selectionner un round disponible !"
MESSAGE_CHOOSE_8_PLAYERS = "Veuillez choisir 8 joueurs en selectionnant" \
                           " l'indice "
MESSAGE_ENCODE_LASTNAME = "tapez le nom du joueur : "
MESSAGE_ENCODE_FIRSTNAME = "tapez le prénom du joueur  : "
MESSAGE_ENCODE_BIRTHDATE = "Entrez la date de naissance du joueur au format" \
                           " DD/MM/YYYY : "
MESSAGE_ENCODE_SEX = "Entrez le genre du joueur (M/F) : "
MESSAGE_ENCODE_CLASSMENT = "Entrez le dernier classement du joueur n° : "
MESSAGE_CONTINUE_ENCODE_PLAYERS = "Voulez-vous continuer à encoder " \
                                  "des joueurs (Y/N) ? "
MESSAGE_CONTINUE_ENCODE_TOURNAMENT = "voulez-vous continuer le tournoi" \
                                     " (Y/N) ?  "
MESSAGE_CONTINUE_ANOTHER_TOURNAMENT = "Voulez-vous encoder un autre tournoi" \
                                      " (Y/N) ? "
MESSAGE_ENCODE_AREA = "Entrez le lieu du tournoi : "
MESSAGE_ENCODE_DATE_TOURNAMENT = "Entrez la date du tournoi au format " \
                                 "DD/MM/YYYY : "
MESSAGE_ENCODE_DESCRIPTION = "Entrez la description du tournoi : "
MESSAGE_SELECT_INDICE_PLAYER = "Selectionnez un indice pour le joueur "
MESSAGE_SELECT_INDICE_TOURNAMENT = "Selectionnez un indice pour le tournoi "
MESSAGE_SELECT_ROUND_RESTART = "Selectionnez un round de redémarrage "
MESSAGE_BEGIN_DATE_ROUND = "Entrez la date de début du round n° {} " \
                           "au format DD/MM/YYYY : "
MESSAGE_BEGIN_TIME_ROUND = "Entrez l'heure de début du round n° {} " \
                           "au format HH:MM : "
MESSAGE_END_DATE_ROUND = "Entrez la date de fin du round n° {} " \
                         "au format DD/MM/YYYY : "
MESSAGE_END_TIME_ROUND = "Entrez l'heure de fin du round n° {} " \
                         "au format HH:MM : "
MESSAGE_END_ROUND = "Les joueur A {} et Joueur B {} ont fini .Donnez" \
                    " le score (0 si nul,1 si A gagnant,2 si B gagnant ) : "
MESSAGE_IF_ROUND_FINISHED = "le round est-il terminé (Y/N) ?  "
MESSAGE_NUMBER_MATCH = "Pour quel match voulez-vous entrer les scores ?  "

"""error messages"""
MESSAGE_BAD_ANSWER_Y_OR_N = "Veuillez encoder 'Y' ou 'N' !"
MESSAGE_BAD_ANSWER_1_OR_2 = "Veuillez encoder 1 ou 2 !"
MESSAGE_WRONG_GAME = "Veuillez encoder 1 ,2 ,3 ou 4 !"
MESSAGE_WRONG_RESULT = "Veuillez encoder 0, 1 ou 2 !"
MESSAGE_WRONG_DATE_FORMAT = "Veuillez encoder la date au format DD/MM/YYYY !"
MESSAGE_WRONG_DATE_INVALID = "La date encodée est invalide !"
MESSAGE_WRONG_TIME_FORMAT = "Veuillez encoder l'heure au format HH:MM"
MESSAGE_WRONG_TIME_INVALID = "L'heure encodée est invalide !"
MESSAGE_NOT_NUMERIC = "Valeur non numerique"
MESSAGE_CLASSMENT_MIN = "Clessement inférieur au minimum"
MESSAGE_CLASSMENT_MAX = "Clessement supérieur au maximum"
MESSAGE_PLAYER_ALLREADY_SELECTED = "Joueur déja selectionné !"
MESSAGE_WRONG_SEX = "Veuillez encoder 'M' ou 'F' !"

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

RESULTS = [0, 1, 2]
GAMES = [1, 2, 3, 4]
CODE_SEXE = ['M', 'F']

"""Constants for tournament"""
AREA_DEFAULT = "A completer"
DESCRIPTION_DEFAULT = "A completer"
"""Constants for players"""
LAST_NAME_DEFAULT = 'A completer'
FIRST_NAME_DEFAULT = 'A completer'
BIRTHDATE_DEFAULT = '01/01/1900'
SEX_DEFAULT = 'A completer'
CLASSMENT_DEFAULT = 400
CLASSMENT_MIN = 400
CLASSMENT_MAX = 3000
SEX_MALE = 'M'
SEX_FEMALE = 'F'
