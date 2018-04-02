import math

import chess


def materiel_noir(board):
    score = 0
    score += board.pieces(1, False).__len__() * 1
    score += board.pieces(2, False).__len__() * 3.2
    score += board.pieces(3, False).__len__() * 3.3
    score += board.pieces(4, False).__len__() * 5.1
    score += board.pieces(5, False).__len__() * 8.8
    return score


def fin_de_jeu(board: chess.Board):
    bonus_malus = 0
    if board.is_game_over():
        result = board.result()
        if board.is_checkmate():
            if result == "1-0":
                bonus_malus += math.inf
            if result == "0-1":
                bonus_malus += -math.inf
        if result == "1/2-1/2":
            sc = _score(board)
            if sc > 0:
                bonus_malus -= 10
            else:  # sc < 0
                bonus_malus += 10
    return bonus_malus


def mobilite(board: chess.Board, player):
    tour_actuel = board.turn
    if player == tour_actuel:
        return board.legal_moves.count()
    if player != tour_actuel:
        board.push(chess.Move.null())
        nbrMoves = board.legal_moves.count()
        board.pop()
        return nbrMoves


def materiel_blanc(board: chess.Board):
    score = 0
    score += board.pieces(1, True).__len__() * 1
    score += board.pieces(2, True).__len__() * 3.2
    score += board.pieces(3, True).__len__() * 3.3
    score += board.pieces(4, True).__len__() * 5.1
    score += board.pieces(5, True).__len__() * 8.8
    return score


def _score(board):
    score = 0
    score -= materiel_noir(board)
    score += materiel_blanc(board)
    score += mobilite(board, True) * 0.1
    score -= mobilite(board, False) * 0.1
    return score


def evaluer(board):
    score = 0
    score += _score(board)
    score += fin_de_jeu(board)
    return score


def evaluer_coup(board: chess.Board, move: chess.Move):
    # not implemented
    return None
