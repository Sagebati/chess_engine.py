import math

import chess
import collections

import IA.evaluation as ev

from util.funcs import creative_move


def ab_max(board: chess.Board, alpha, beta, profondeur):
    """
    :param board: the board of the game
    :param alpha: alpha val
    :param beta: beta val
    :param profondeur: profondeur
    :return: the evaluatuin of the branch
    """
    if profondeur == 0 or board.is_game_over():
        return ev.evaluer(board)
    best_eval = -math.inf
    for coup in board.legal_moves:
        board.push(coup)
        best_eval = max(best_eval, ab_min(board, alpha, beta, profondeur - 1))
        board.pop()
        if best_eval >= beta:
            return best_eval
        alpha = max(alpha, best_eval)
    return best_eval


def ab_min(board: chess.Board, alpha, beta, profondeur: int):
    """
    :param board: board of the chess game
    :param alpha: alpha
    :param beta: beta
    :param profondeur: profondeur
    :return: the branch evaluation
    """
    if profondeur == 0 or board.is_game_over():
        return ev.evaluer(board)
    best_eval = math.inf
    for coup in board.legal_moves:
        board.push(coup)
        best_eval = min(best_eval, ab_max(board, alpha, beta, profondeur - 1))
        board.pop()
        if best_eval <= alpha:
            return best_eval
        beta = min(beta, best_eval)
    return best_eval


def best_play(board: chess.Board, player: bool, profondeur: int = 5) -> chess.Move:
    best_moves = collections.deque(2 * [(0, 0)], 2)
    alpha, beta = -math.inf, math.inf
    if player:  # Max
        best_eval = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            ab = ab_min(board, alpha, beta, profondeur - 1)
            board.pop()
            if ab > best_eval:
                best_eval = ab
                best_moves.appendleft((coup, ab))
            alpha = max(alpha, ab)
    else:  # Min Joueur Noir
        best_eval = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            ab = ab_max(board, alpha, beta, profondeur - 1)
            board.pop()
            if ab < best_eval:
                best_eval = ab
                best_moves.appendleft((coup, ab))
            beta = min(ab, beta)
    return creative_move(best_moves)
