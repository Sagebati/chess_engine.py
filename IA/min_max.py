import math

import chess
import collections

import IA.evaluation as ev
from util.funcs import creative_move


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

    best_moves = collections.deque(2 * [(0, 0)], 2)

    val_min = -math.inf
    val_max = math.inf
    for move in board.legal_moves:
        if player:
            board.push(move)
            val = _min(board, profondeur)
            board.pop()
            if val > val_min:
                val_min = val
                best_moves.appendleft((move, val))
        else:
            board.push(move)
            val = _max(board, profondeur)
            board.pop()
            if val < val_max:
                val_max = val
                best_moves.appendleft((move, val))

    return creative_move(best_moves)
