import chess


def materiel_noir(board):
    score = 0
    score += board.pieces(1, False).__len__() * 1
    score += board.pieces(2, False).__len__() * 3.2
    score += board.pieces(3, False).__len__() * 3.3
    score += board.pieces(4, False).__len__() * 5.1
    score += board.pieces(5, False).__len__() * 8.8
    return score


def mobilite(board: chess.Board, player):
    turn_actuel = board.turn
    if player == turn_actuel:
        return board.legal_moves.count()
    if player != turn_actuel:
        board.push(chess.Move.null())
        nbrMoves = board.legal_moves.count()
        board.pop()
        return nbrMoves


def materiel_blanc(board:chess.Board):
    score = 0
    score += board.pieces(1, True).__len__() * 1
    score += board.pieces(2, True).__len__() * 3.2
    score += board.pieces(3, True).__len__() * 3.3
    score += board.pieces(4, True).__len__() * 5.1
    score += board.pieces(5, True).__len__() * 8.8
    return score


def evaluer(board):
    score = 0
    score -= materiel_noir(board)
    score += materiel_blanc(board)
    score += mobilite(board, True) * 0.3
    score -= mobilite(board, False) * 0.3
    return score
