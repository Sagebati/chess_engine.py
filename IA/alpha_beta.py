import chess
import math
import IA.evaluation as ev


def ab_max(board: chess.Board, alpha, beta, profondeur):
    if profondeur == 0:
        return ev.evaluer(board)
    val = -math.inf
    for coup in board.legal_moves:
        board.push(coup)
        val = max(val, ab_min(board, alpha, beta, profondeur - 1))
        board.pop()
        if val >= beta:
            return val
        alpha = max(beta, val)


def ab_min(board: chess.Board, alpha, beta, profondeur):
    if profondeur == 0:
        return ev.evaluer(board)
    val = math.inf
    for coup in board.legal_moves:
        print(coup)
        board.push(coup)
        val = min(val, ab_max(board, alpha, beta, profondeur - 1))
        board.pop()
        if val <= alpha:
            return val
        beta = min(beta, val)


def best_play(board, player, profondeur=5):
    if player:
        val_min = -math.inf
        mv = None
        for coup in board.legal_moves:
            board.push(coup)
            val_max = ab_min(board, -math.inf, math.inf, profondeur - 1)
            if val_max > val_min:
                val_min = val_max
                mv = coup
        return mv
