import IA.MinMax as mm
import math


def alphabeta(board, profondeur):
    alpha = -math.inf
    beta = math.inf

    val = math.inf
    for coup in board.legal_moves:
        board.push_uci(coup.uci())
        val = max(val, _min(board, profondeur - 1, alpha, beta))
        board.pop()
        if alpha >= val:
            return val
        beta = min(beta, val)


def _max(board, profondeur, alpha, beta):
    if profondeur == 0:
        return mm.evaluer_jeu(board)
    val = math.inf
    for coup in board.legal_moves:
        board.push_uci(coup.uci())
        val = max(val, _min(board, profondeur - 1, alpha, beta))
        board.pop()
        if alpha >= val:
            return val
        beta = min(beta, val)


def _min(board, profondeur, alpha, beta):
    if profondeur == 0:
        return mm.evaluer_jeu(board)
    val = -math.inf
    for coup in board.legal_moves:
        board.push_uci(coup.uci())
        val = max(val, _max(board, profondeur - 1, alpha, beta))
        board.pop()
        if alpha <= val:
            return val
        alpha = max(beta, val)
