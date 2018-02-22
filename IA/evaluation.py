import chess


def materiel_noir(board):
    score = 0
    score += board.pieces(1, False).__len__() * 1
    score += board.pieces(2, False).__len__() * 3.2
    score += board.pieces(3, False).__len__() * 3.3
    score += board.pieces(4, False).__len__() * 5.1
    score += board.pieces(5, False).__len__() * 8.8
    return score


def fin_de_jeu(board: chess.Board, player):
    bonus_malus = 0
    if board.is_game_over():
        result = board.result()
        if board.is_checkmate():
            if result == "1-0":
                bonus_malus += 50
            if result == "0-1":
                bonus_malus += -50
        if result == "1/2-1/2":
            sc = _score(board)
            if sc > 0:
                if player:
                    bonus_malus -= sc/2
                else:
                    bonus_malus += sc/4
            else: # sc < 0
                if player:
                    bonus_malus += sc/4
                else:
                    bonus_malus -= sc/2
    return bonus_malus


def mobilite(board: chess.Board, player):
    turn_actuel = board.turn
    if player == turn_actuel:
        return board.legal_moves.count()
    if player != turn_actuel:
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
    score += mobilite(board, True) * 0.3
    score -= mobilite(board, False) * 0.3
    return score


def evaluer(board):
    score = 0
    score += _score(board)
    score += fin_de_jeu(board, board.turn)
    return score
