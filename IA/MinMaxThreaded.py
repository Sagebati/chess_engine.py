from threading import Thread

import chess
import math


def evaluer_jeu(board):
    score = 0
    score += board.pieces(1, board.turn).__len__() * 1
    score += board.pieces(2, board.turn).__len__() * 3
    score += board.pieces(3, board.turn).__len__() * 3
    score += board.pieces(4, board.turn).__len__() * 5
    score += board.pieces(5, board.turn).__len__() * 9
    score += board.legal_moves.count() * 0.5
    score += 10 if board.is_checkmate() else 0

    return score


def min(board, profondeur):
    """
    :param board: le tableau du jeu
    :type board: chess.Board
    :param profondeur: profondeur de l'algo
    :type profondeur: int
    """
    if profondeur == 0 or board.is_game_over():
        return evaluer_jeu(board)

    min_val = 99999999

    for play in board.legal_moves:
        board.push_uci(play.uci())
        # board_clone = board.copy()
        # board_clone.push_uci(play.uci())
        val = max(board, profondeur - 1)

        if val < min_val:
            min_val = val

        board.pop()

    return min_val


def max(board, profondeur):
    """
    :param board: le tableau du jeu
    :type board: chess.Board
    :param profondeur: profondeur de l'algo
    :type profondeur: int
    """
    if profondeur == 0 or board.is_game_over():
        return evaluer_jeu(board)

    max_val = -999999999
    vals = []
    for play in board.legal_moves:
        board.push_uci(play.uci())

        val = min(board, profondeur - 1)

        if val > max_val:
            max_val = val

        # del board_clone  # on efface le board cloné
        board.pop()

    return max_val


def best_play(board, profondeur=5):
    """
    :param profondeur: profondeur de l'algorithme
    :param board: chess.Board
    :param player:
    :return:
    """
    val_max = -999999999
    best_move = None
    for move in board.legal_moves:
        board.push_uci(move.uci())
        # board_clone = board.copy()
        # board_clone.push_uci(move.uci())
        val = min(board, profondeur)
        if val > val_max:
            val_max = val
            best_move = move

        # del board_clone
        board.pop()
    return best_move

class ThreadMethod(Thread):
    def __init__(self, tabRes,fonction):
        Thread.__init__(self)
        self.tabRes = tabRes
        self.f = fonction

    def run(self):
        


