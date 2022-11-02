NUMBER_GAMES = 4

class Round:
    """chess round"""

    def __init__(self,name_round,begindate,begintime,enddate,endtime,games):
        self.name_round = name_round
        self.begindate = begindate
        self.begintime = begintime
        self.enddate = enddate
        self.endtime = endtime
        self.games = games