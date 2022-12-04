NOMBRE_JOUEURS = 8


class Player:
    """Chess Player"""

    def __init__(self, player_id, lastname, firstname, birthdate, sex, classment, score = 0):
        """Has lastname,firstname, birthdate sex and classment"""
        self.player_id = player_id
        self.lastname = lastname
        self.firstname = firstname
        self.birthdate = birthdate
        self.sex = sex
        self.classment = classment
        self.score = score
