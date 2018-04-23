import random

import collections


def creative_move(fifo: collections.deque):
    """
    Function hat return and random move between moves in the dequeu
    :param fifo:
    :return:
    """
    epsilon = 0.3
    best_eval = fifo[0][1]

    # Creating a list with move with 0.5 difference with the best move
    coup_possibles = [coupeval for coupeval in fifo if best_eval - epsilon <= coupeval[1] <= best_eval + epsilon]

    return random.choice(coup_possibles)[0]
