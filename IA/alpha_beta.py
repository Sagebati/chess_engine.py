import chess
import math
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
    if player:
        val_min = -math.inf
        for coup in board.legal_moves:
            board.push(coup)
            val_max = ab_min(board, -math.inf, math.inf, profondeur - 1)
            board.pop()
            if val_max > val_min:
                val_min = val_max
                mv = coup
    else:
        val_max = math.inf
        for coup in board.legal_moves:
            board.push(coup)
            val_min = ab_max(board, -math.inf, math.inf, profondeur - 1)
            board.pop()
            if val_min < val_max:
                val_max = val_min
                mv = coup
    return mv
