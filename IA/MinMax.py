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

player = True

def evalPiece(piece:chess.Piece):


def evaluerJeu(board : chess.Board):
    pieces = board.pieces(player)
    score = 0
    def f(x): return {
        1:1,
        2:3.2,
        3:3.33,
        4:5.1,
        5:8.8
    }.get(x)
    for p in pieces:
        score += f(p.type)


def min(board:chess.Board, profondeur):
    if profondeur == 0 or board.is_game_over():
        return


def bestPlay(board: chess.Board, player):
    """
    :param board: chess.Board
    :param player:
    :return:
    """
    boardWork = board.copy()
    max = 999999
    for move in board.legal_moves:
        boardWork.push(move)



