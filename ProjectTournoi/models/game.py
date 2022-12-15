"""definition of game"""


class Game:
    def __init__(self, game_id, player_a, player_b, result=None):
        self.game_id = game_id
        self.player_a = player_a
        self.player_b = player_b
        self.result = result
