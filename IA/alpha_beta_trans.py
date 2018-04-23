import math

import chess
import chess.polyglot as zb
import collections

import IA.evaluation as ev
import util.funcs
from util.tt import HashItem


def ab_max(board: chess.Board, alpha: int, beta: int, depth: int, tt: {}):
    if depth == 0 or board.is_game_over():
        return ev.evaluer(board)
    best_eval = -math.inf
    for coup in board.legal_moves:
        board.push(coup)
        h = zb.zobrist_hash(board)
        if h in tt.keys():
            it: HashItem = tt[h]
            if it.depth <= depth:
                ab = tt[h].evaluation
            else:
                ab = ab_min(board, alpha, beta, depth - 1, tt)
        else:
            ab = ab_min(board, alpha, beta, depth - 1, tt)
        board.pop()
        best_eval = max(best_eval, ab)
        if best_eval >= beta:
            tt[h] = HashItem(h, depth, best_eval, (alpha, beta))
            return best_eval
        alpha = max(alpha, best_eval)
        tt[h] = HashItem(h, depth, best_eval, (alpha, beta))
    return best_eval


def ab_min(board: chess.Board, alpha: int, beta: int, depth: int, tt: {}):
    if depth == 0 or board.is_game_over():
        return ev.evaluer(board)
    best_eval = math.inf
    for coup in board.legal_moves:
        board.push(coup)
        h = zb.zobrist_hash(board)
        if h in tt.keys():
            it: HashItem = tt[h]
            if it.depth <= depth:
                ab = tt[h].evaluation
            else:
                ab = ab_max(board, alpha, beta, depth - 1, tt)
        else:
            ab = ab_max(board, alpha, beta, depth - 1, tt)
        board.pop()
        best_eval = min(best_eval, ab)
        if best_eval <= alpha:
            tt[h] = HashItem(h, depth, best_eval, (alpha, beta))
            return best_eval
        beta = min(beta, best_eval)
        tt[h] = HashItem(h, depth, best_eval, (alpha, beta))
    return best_eval


def best_play(board: chess.Board, player: bool, depth: int = 5):
    tt = {}
    best_moves = collections.deque(2 * [(0, 0)], 2)
    alpha, beta = -math.inf, math.inf
    if player:  # Max Blanc
        best_val = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            h = zb.zobrist_hash(board)
            if h in tt.keys():
                ab = tt[h].evaluation
            else:
                ab = ab_min(board, alpha, beta, depth - 1, tt)
            if ab > best_val:
                best_val = ab
                best_moves.appendleft((coup, ab))
            alpha = max(alpha, ab)
            board.pop()
    else:  # Min Noir
        best_val = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            h = zb.zobrist_hash(board)
            if h in tt.keys():
                ab = tt[h].evaluation
            else:
                ab = ab_max(board, alpha, beta, depth - 1, tt)
            if ab < best_val:
                best_val = ab
                best_moves.appendleft((coup, ab))
            beta = min(beta, ab)
            board.pop()
    return util.funcs.creative_move(best_moves)
