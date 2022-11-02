NUMBER_ROUNDS = 4

class Tournament:
    """Chess Tournament"""

    def __init__(self,name,area,date,rounds,description,players):
        """Has name,area, date, number of rounds,description"""
        self.name = name
        self.area = area
        self.date = date
        self.rounds = rounds
        self.description = description
        self.players = players