
def get_result_player(list, element):
    for ind in range(len(list)):
        if list[ind].player_id == element:
            return ind

"""Search if player 1 and player 2 played already """


def search_couple(list, element_a, element_b):
    for indr in range(len(list)):
        for indg in range(len(list[indr].games)):
            if list[indr].games[indg].player_A == element_a and list[indr].games[indg].player_B == element_b:
                return True
            if list[indr].games[indg].player_B == element_a and list[indr].games[indg].player_A == element_b:
                return True
    return False
