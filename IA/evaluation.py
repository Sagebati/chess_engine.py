import chess

from IA.psq import *


def materiel(board: chess.Board, color):
    score = 0
    score += board.pieces(chess.PAWN, color).__len__() * 100
    score += board.pieces(chess.KNIGHT, color).__len__() * 320
    score += board.pieces(chess.BISHOP, color).__len__() * 330
    score += board.pieces(chess.ROOK, color).__len__() * 510
    score += board.pieces(chess.QUEEN, color).__len__() * 880
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
            sc = materiel_mob(board)
            if sc > 0:
                bonus_malus -= 2
            else:  # sc < 0
                bonus_malus += 2
    return bonus_malus


def mobilite(board: chess.Board, color):
    tour_actuel = board.turn
    if color == tour_actuel:
        return board.legal_moves.count()
    if color != tour_actuel:
        board.push(chess.Move.null())
        nbr_moves = board.legal_moves.count()
        board.pop()
        return nbr_moves


def materiel_mob(board):
    score = 0
    score -= materiel(board, False)
    score += materiel(board, True)
    score -= mobilite(board, False) * 20
    score += mobilite(board, True) * 20
    return score


def psq_tables(board: chess.Board):
    score = 0
    pawns_w = board.pieces(chess.PAWN, chess.WHITE)
    pawns_b = board.pieces(chess.PAWN, chess.BLACK)
    for i in pawns_w:
        score += psq_tables_w[chess.PAWN][i]
    for i in pawns_b:
        score -= psq_tables_b[chess.PAWN][i]

    knights_w = board.pieces(chess.KNIGHT, chess.WHITE)
    knights_b = board.pieces(chess.KNIGHT, chess.BLACK)
    for i in knights_w:
        score += psq_tables_w[chess.KNIGHT][i]
    for i in knights_b:
        score -= psq_tables_b[chess.KNIGHT][i]
    return score


def castling(board: chess.Board, color: bool) -> int:
    score = 0
    score += 40 if board.has_kingside_castling_rights(color) else 0
    score += 40 if board.has_queenside_castling_rights(color) else 0
    return score


def evaluer(board):
    score = 0
    score += materiel_mob(board)
    score += castling(board, True)
    score -= castling(board, True)
    score += fin_de_jeu(board)
    score += psq_tables(board)
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
