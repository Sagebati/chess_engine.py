import math

import chess
import chess.polyglot as zb
import collections

import IA.evaluation as ev

from util.tt import HashItem


def ab_max(board: chess.Board, alpha: int, beta: int, profondeur: int, tt: {}):
    if profondeur == 0 or board.is_game_over():
        hash = zb.zobrist_hash(board)
        note = ev.evaluer(board)
        tt[hash] = HashItem(hash, profondeur, note, (alpha, beta))
        return note
    val = -math.inf
    for coup in board.legal_moves:
        h = zb.zobrist_hash(board)
        if h in tt.keys():
            alpha, beta = tt[h].alphabeta
        board.push(coup)
        val = max(val, ab_min(board, alpha, beta, profondeur - 1, tt))
        board.pop()
        if val >= beta:
            return val
        alpha = max(alpha, val)
    return val


def ab_min(board: chess.Board, alpha: int, beta: int, profondeur: int, tt: {}):
    if profondeur == 0 or board.is_game_over():
        hash = zb.zobrist_hash(board)
        note = ev.evaluer(board)
        tt[hash] = HashItem(hash, profondeur, note, (alpha, beta))
        return note
    val = math.inf
    for coup in board.legal_moves:
        board.push(coup)
        zb_hash = zb.zobrist_hash(board)
        if zb_hash in tt.keys():
            alpha, beta = tt[zb_hash].alphabeta
        val = min(val, ab_max(board, alpha, beta, profondeur - 1, tt))
        board.pop()
        if val <= alpha:
            return val
        beta = min(beta, val)
    return val


def best_play(board, player, profondeur=5):
    mv = None
    tt = {}
    # doing a dequeu of fixed lenght (2nd param)
    best_moves = collections.deque(2 * [(0, 0)], 2)
    if player:
        val_min = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            zob_hash = zb.zobrist_hash(board)
            if zob_hash in tt.keys():
                mv = tt[zob_hash]
            else:
                val_max = ab_min(board, -math.inf, math.inf, profondeur - 1, tt)
                if val_max > val_min:
                    val_min = val_max
                    mv = coup
                    best_moves.appendleft((coup, val_max))
            board.pop()
    else:
        val_max = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            zob_hash = zb.zobrist_hash(board)
            if zob_hash in tt.keys():
                mv = tt[zob_hash]
            else:
                val_min = ab_max(board, -math.inf, math.inf, profondeur - 1, tt)
                if val_min < val_max:
                    val_max = val_min
                    mv = coup
                    best_moves.appendleft((coup, val_min))
            board.pop()
    return mv
