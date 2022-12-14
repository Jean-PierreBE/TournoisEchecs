"""round"""

class Round:
    """chess round"""

    def __init__(self, round_id, begindate, begintime, enddate, endtime, games):
        self.round_id = round_id
        self.begindate = begindate
        self.begintime = begintime
        self.enddate = enddate
        self.endtime = endtime
        self.games = games
