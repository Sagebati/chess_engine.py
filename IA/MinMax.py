'''
fonction jouer : void
     max_val <- -infini
     Pour tous les coups possibles
          simuler(coup_actuel)
          val <- Min(etat_du_jeu, profondeur)
          si val > max_val alors
               max_val <- val
               meilleur_coup <- coup_actuel
          fin si
          annuler_coup(coup_actuel)
     fin pour
     jouer(meilleur_coup)
fin fonction
'''

import chess
import math


def evaluer_jeu(board: chess.Board):
    score = 0
    score = board.pieces(1, board.turn).__len__() * 1
    score = board.pieces(2, board.turn).__len__() * 3
    score = board.pieces(3, board.turn).__len__() * 3
    score = board.pieces(4, board.turn).__len__() * 5
    score = board.pieces(5, board.turn).__len__() * 9
    score = board.legal_moves.count() * 0.5

    return score


def min(board: chess.Board, profondeur):
    if profondeur == 0 or board.is_game_over():
        return evaluer_jeu(board)

    min_val = math.inf

    for play in board.legal_moves:
        board_clone = board.copy()
        board_clone.push_uci(play.uci())
        val = max(board_clone, profondeur - 1)

        if val < min_val:
            min_val = val

        del board_clone  # on efface le board cloné

    return min_val


def max(board: chess.Board, profondeur):
    if profondeur == 0 or board.is_game_over():
        return evaluer_jeu(board)

    max_val = -math.inf

    for play in board.legal_moves:
        board_clone = board.copy()
        board_clone.push_uci(play.uci())
        val = max(board_clone, profondeur - 1)

        if val > max_val:
            max_val = val

        del board_clone  # on efface le board cloné

    return max_val


def bestPlay(board: chess.Board, profondeur=5):
    """
    :param board: chess.Board
    :param player:
    :return:
    """
    val_max = -math.inf
    best_play = None
    for move in board.legal_moves:
        board_clone = board.copy()
        #print(move.uci())
        board_clone.push_uci(move.uci())
        val = min(board_clone, profondeur)

        if val > val_max:
            val_max = val
            best_play = move

        del board_clone

    return best_play
