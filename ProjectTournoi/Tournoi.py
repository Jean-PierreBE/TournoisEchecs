"""Procedures"""

def create_game(players,round,numbergame):
    """allocate players for game"""
    games = []

    last_player = 0
    for num_game in range(numbergame):
        pref_game = 'Game_' + str(round) + str(num_game+1)
        player_A = players[last_player].player_id
        player_B = players[last_player + 1].player_id
        last_player = last_player + 2
        game = [pref_game,player_A,player_B,0]
        games.append(game)

    return games