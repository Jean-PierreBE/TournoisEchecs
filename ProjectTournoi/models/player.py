NOMBRE_JOUEURS = 8

class Player:
    """Chess Player"""

    def __init__(self,name,vorname,birthdate,sex,classment,score):
        """Has name,vorname birthdate sex and classment"""
        self.name = name
        self.vorname = vorname
        self.birthdate = birthdate
        self.sex = sex
        self.classment = classment
        self.score = score