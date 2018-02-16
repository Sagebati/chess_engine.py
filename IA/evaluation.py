def evaluer_jeu_noir(board):
    score = 0
    score += board.pieces(1, False).__len__() * 1
    score += board.pieces(2, False).__len__() * 3.2
    score += board.pieces(3, False).__len__() * 3.3
    score += board.pieces(4, False).__len__() * 5.1
    score += board.pieces(5, False).__len__() * 8.8
    #score += board.legal_moves.count() * 0.5
    """for coups in board.legal_moves:
        type = board.piece_type_at(coups.from_square)
        if type == 1:
            score += 0.1
        if type == 2:
            score += 0.2
        if type == 3:
            score += 0.3
        if type == 4:
            score += 0.4
        if type == 5:
            score += 0.5
        if type == 6:
            score += 0.2
    """
    return score


def evaluer_jeu_blanc(board):
    score = 0
    score += board.pieces(1, True).__len__() * 1
    score += board.pieces(2, True).__len__() * 3.2
    score += board.pieces(3, True).__len__() * 3.3
    score += board.pieces(4, True).__len__() * 5.1
    score += board.pieces(5, True).__len__() * 8.8
    #score += board.legal_moves.count() * 0.5
    """for coups in board.legal_moves:
        type = board.piece_type_at(coups.from_square)
        if type == 1:
            score += 0.1
        if type == 2:
            score += 0.2
        if type == 3:
            score += 0.3
        if type == 4:
            score += 0.4
        if type == 5:
            score += 0.5
        if type == 6:
            score += 0.2
    """
    return score

def evaluer(board):
    score = 0
    score -= evaluer_jeu_noir(board)
    score += evaluer_jeu_blanc(board)
