import math

import chess
import collections

import IA.evaluation as ev
from util.funcs import creative_move


def ab_max(board: chess.Board, alpha, beta, profondeur):
    if profondeur == 0 or board.is_game_over():
        return ev.evaluer(board)
    val = -math.inf
    for coup in board.legal_moves:
        board.push(coup)
        val = max(val, ab_min(board, alpha, beta, profondeur - 1))
        board.pop()
        if val >= beta:
            return val
        alpha = max(alpha, val)
    return val


def ab_min(board: chess.Board, alpha, beta, profondeur):
    if profondeur == 0 or board.is_game_over():
        return ev.evaluer(board)
    val = math.inf
    for coup in board.legal_moves:
        board.push(coup)
        val = min(val, ab_max(board, alpha, beta, profondeur - 1))
        board.pop()
        if val <= alpha:
            return val
        beta = min(beta, val)
    return val


def best_play(board: chess.Board, player: bool, profondeur: int = 5) -> chess.Move:
    # doing a deque of fixed length (2nd param)
    best_moves = collections.deque(2 * [(0, 0)], 2)
    if player:
        val_min = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            val_max = ab_min(board, -math.inf, math.inf, profondeur - 1)
            board.pop()
            if val_max > val_min:
                val_min = val_max
                best_moves.appendleft((coup, val_max))
    else:
        val_max = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            val_min = ab_max(board, -math.inf, math.inf, profondeur - 1)
            board.pop()
            if val_min < val_max:
                val_max = val_min
                best_moves.appendleft((coup, val_min))
    return creative_move(best_moves)
