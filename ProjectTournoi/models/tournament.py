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

    def set_result(self, result, inda, indb):
        """
        - result = 0 match nul
        - result 1 player_A win
        - result 2 player_ B win
        :param result:
        :return:
        """
        self.result = result
        if result == 0:
            self.players[inda].score += 0.5
            self.players[indb].score += 0.5

        if result == 1:
            self.players[inda].score += 1
            self.players[indb].score += 0

        if result == 2:
            self.players[inda].score += 0
            self.players[indb].score += 1
