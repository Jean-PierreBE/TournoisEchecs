
def get_result_player(list, element):
    for ind in range(len(list)):
        if list[ind].player_id == element:
            return ind


"""Search if player 1 and player 2 played already """


def search_couple(list, element_a, element_b):
    for ind in range(len(list)):
        if list[ind].player_A == element_a and list[ind].player_B == element_b:
            return True
        if list[ind].player_B == element_a and list[ind].player_A == element_b:
            return True
    return False
