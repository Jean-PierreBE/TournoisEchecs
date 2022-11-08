NUMBER_ROUNDS = 4


class Tournament:
    """Chess Tournament"""

    def __init__(self, tournament_id, area, date, description, rounds, players):
        """Has name,area, date, number of rounds,description"""
        self.tournament_id = tournament_id
        self.area = area
        self.date = date
        self.description = description
        self.rounds = rounds
        self.players = players
