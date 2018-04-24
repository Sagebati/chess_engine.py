import math

import chess
import collections

import eval.evaluation as ev
from util.funcs import creative_move


def ab_max(board: chess.Board, alpha, beta, depth) -> int:
    """
    :param board: the board of the game
    :param alpha: alpha val
    :param beta: beta val
    :param depth: depth
    :return: the evaluation of the branch
    """
    if depth == 0 or board.is_game_over():
        return ev.evaluate(board)
    best_eval = -math.inf
    for coup in board.legal_moves:
        board.push(coup)
        best_eval = max(best_eval, ab_min(board, alpha, beta, depth - 1))
        board.pop()
        if best_eval >= beta:
            return best_eval
        alpha = max(alpha, best_eval)
    return best_eval


def ab_min(board: chess.Board, alpha, beta, depth: int) -> int:
    """
    :param board: board of the chess game
    :param alpha: alpha
    :param beta: beta
    :param depth: profondeur
    :return: the branch evaluation
    """
    if depth == 0 or board.is_game_over():
        return ev.evaluate(board)
    best_eval = math.inf
    for coup in board.legal_moves:
        board.push(coup)
        best_eval = min(best_eval, ab_max(board, alpha, beta, depth - 1))
        board.pop()
        if best_eval <= alpha:
            return best_eval
        beta = min(beta, best_eval)
    return best_eval


def best_play(board: chess.Board, player: bool, depth: int = 5) -> chess.Move:
    best_moves = collections.deque(2 * [(0, 0)], 2)
    alpha, beta = -math.inf, math.inf
    if player:  # Max
        best_eval = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            ab = ab_min(board, alpha, beta, depth - 1)
            board.pop()
            if ab > best_eval:
                best_eval = ab
                best_moves.appendleft((coup, ab))
            alpha = max(alpha, ab)
    else:  # Min Joueur Noir
        best_eval = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            ab = ab_max(board, alpha, beta, depth - 1)
            board.pop()
            if ab < best_eval:
                best_eval = ab
                best_moves.appendleft((coup, ab))
            beta = min(ab, beta)
    return creative_move(best_moves)
