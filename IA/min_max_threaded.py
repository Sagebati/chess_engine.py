import chess
import math

import IA.evaluation as ev
import threading


def _min(board, profondeur):
    """
    :param board: le tableau du jeu
    :type board: chess.Board
    :param profondeur: profondeur de l'algo
    :type profondeur: int
    """
    if profondeur == 0 or board.is_game_over():
        return ev.evaluer(board)

    val = math.inf
    for play in board.legal_moves:
        board.push(play)
        val = min(val, _max(board, profondeur - 1))
        board.pop()

    return val


def _max(board, profondeur):
    """
    :param board: le tableau du jeu
    :type board: chess.Board
    :param profondeur: profondeur de l'algo
    :type profondeur: int
    """
    if profondeur == 0 or board.is_game_over():
        return ev.evaluer(board)

    val = -math.inf

    for play in board.legal_moves:
        board.push(play)
        val = max(val, _min(board, profondeur - 1))
        board.pop()
    return val


def best_play(board, player, profondeur=5):
    """
    :param profondeur: profondeur de l'algorithme
    :param board: chess.Board
    :param player: boolean
    :return: chess.Move
    """
    val_min = -math.inf
    val_max = math.inf
    best_move = None
    for move in board.legal_moves:
        if player:
            board.push(move)
            val = _min(board, profondeur)
            board.pop()
            if val > val_min:
                val_min = val
                best_move = move
        else:
            board.push(move)
            val = _max(board, profondeur)
            board.pop()
            if val < val_max:
                val_max = val
                best_move = move
    return best_move



class minimax(threading.Thread):
    def __init__(self,tab_res, id):
        self.tab_res = tab_res
        self.id = id

    def run(self, func):
        tab_res[i] = func(board)

