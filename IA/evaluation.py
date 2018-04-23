import math

import chess


def materiel_noir(board: chess.Board):
    score = 0
    score += board.pieces(1, False).__len__() * 1
    score += board.pieces(2, False).__len__() * 3.2
    score += board.pieces(3, False).__len__() * 3.3
    score += board.pieces(4, False).__len__() * 5.1
    score += board.pieces(5, False).__len__() * 8.8
    return score


def materiel_blanc(board: chess.Board):
    score = 0
    score += board.pieces(1, True).__len__() * 1
    score += board.pieces(2, True).__len__() * 3.2
    score += board.pieces(3, True).__len__() * 3.3
    score += board.pieces(4, True).__len__() * 5.1
    score += board.pieces(5, True).__len__() * 8.8
    return score


def fin_de_jeu(board: chess.Board):
    bonus_malus = 0
    if board.is_game_over():
        result = board.result()
        if board.is_checkmate():
            if result == "1-0":
                bonus_malus += 99999
            if result == "0-1":
                bonus_malus -= 99999
        if result == "1/2-1/2":
            sc = _score(board)
            if sc > 0:
                bonus_malus -= 2
            else:  # sc < 0
                bonus_malus += 2
    return bonus_malus


def mobilite(board: chess.Board, player):
    tour_actuel = board.turn
    if player == tour_actuel:
        return board.legal_moves.count()
    if player != tour_actuel:
        board.push(chess.Move.null())
        nbr_moves = board.legal_moves.count()
        board.pop()
        return nbr_moves


def _score(board):
    score = 0
    score -= materiel_noir(board)
    score += materiel_blanc(board)
    score -= mobilite(board, False) * 0.1
    score += mobilite(board, True) * 0.1
    return score


def evaluer(board):
    score = 0
    score += _score(board)
    score += fin_de_jeu(board)
    return score


"""
def sortMoves(board: chess.Board, moves: [chess.Move]):
    squaresQ = board.pieces(5, not board.turn)
    squaresT = board.pieces(4, not board.turn)
    squaresC = board.pieces(3, not board.turn)
    squaresF = board.pieces(2, not board.turn)
    squaresP = board.pieces(1, not board.turn)
    squaresR = board.pieces(6, not board.turn)

    moves_notes = []
    for m in moves:
        if m.to_square == squaresQ:
            moves_notes.append()
            """
