import chess


def evaluer_jeu(board):
    score = 0
    score += board.pieces(1, board.turn).__len__() * 1
    score += board.pieces(2, board.turn).__len__() * 3.2
    score += board.pieces(3, board.turn).__len__() * 3.3
    score += board.pieces(4, board.turn).__len__() * 5.1
    score += board.pieces(5, board.turn).__len__() * 8.8
    score += board.legal_moves.count() * 0.5
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
        val = max(board, profondeur - 1)
        board.pop()
        if val < min_val:
            min_val = val


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

    for play in board.legal_moves:
        board.push_uci(play.uci())
        val = min(board, profondeur - 1)
        board.pop()
        if val > max_val:
            max_val = val

    return max_val


def best_play(board, profondeur=5):
    """
    :param profondeur: profondeur de l'algorithme
    :param board: chess.Board
    :param player:
    :return:
    """
    val_min = 999999999
    best_move = None
    for move in board.legal_moves:
        board.push_uci(move.uci())
        val = max(board, profondeur)
        board.pop()
        if val < val_min:
            val_min = val
            best_move = move

        # del board_clone
    return best_move

