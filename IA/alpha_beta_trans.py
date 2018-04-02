import math
import random

import chess
import chess.polyglot as zb
import collections

import IA.evaluation as ev


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


def best_play(board, player, profondeur=5):
    mv = None
    tt = {}
    # doing a dequeu of fixed lenght (2nd param)
    best_moves = collections.deque(2 * [(0, 0)], 2)
    if player:
        val_min = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            hash = zb.zobrist_hash(board)
            if hash in tt.keys():
                mv = tt[hash]
            else:
                val_max = ab_min(board, -math.inf, math.inf, profondeur - 1)
                if val_max > val_min:
                    val_min = val_max
                    mv = coup
                    best_moves.appendleft((coup, val_max))
                    tt[zb.zobrist_hash(board)] = mv
            board.pop()
    else:
        val_max = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            hash = zb.zobrist_hash(board)
            if hash in tt.keys():
                mv = tt[hash]
            else:
                val_min = ab_max(board, -math.inf, math.inf, profondeur - 1)
                if val_min < val_max:
                    val_max = val_min
                    mv = coup
                    best_moves.appendleft((coup, val_min))
                    tt[zb.zobrist_hash(board)] = mv
            board.pop()
    return mv


def creative_move(fifo: collections.deque):
    epsilon = 0.5
    best_eval = fifo[0][1]

    # Creating a list with move with 0.5 difference with the best move
    coup_possibles = [coupeval for coupeval in fifo if best_eval - epsilon <= coupeval[1] <= best_eval + epsilon]

    return random.choice(coup_possibles)[0]
