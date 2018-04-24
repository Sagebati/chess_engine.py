from eval.psq import *


def material(board: chess.Board, color):
    score = 0
    score += board.pieces(chess.PAWN, color).__len__() * 100
    score += board.pieces(chess.KNIGHT, color).__len__() * 320
    score += board.pieces(chess.BISHOP, color).__len__() * 330
    score += board.pieces(chess.ROOK, color).__len__() * 510
    score += board.pieces(chess.QUEEN, color).__len__() * 880
    return score


def game_over(board: chess.Board):
    """
    Function that return bonuses or maluses.
    if the player if winning the
    :param board: chess.Board
    :return: the score
    """
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
                bonus_malus -= 300
            else:  # sc < 0
                bonus_malus += 300
    return bonus_malus


def mobility(board: chess.Board, color):
    """
    Function that evaluates the mobility of the players
    :param board: chess.Board
    :param color: chess.WHITE || chess.BLACK
    :return: return the number of moves of the color
    """
    if color == board.turn:
        return board.legal_moves.count()
    if color != board.turn:
        board.push(chess.Move.null())
        nbr_moves = board.legal_moves.count()
        board.pop()
        return nbr_moves


def psq_tables(board: chess.Board, is_endgame: bool = False) -> int:
    """
    Function that returns the heuristic of the board in adequately with the
    psq tables in psq.pyx
    TODO: Better understanding and use this tables only when needed
    :param board: the board needed to calculate the
    :param is_endgame: True is the game is about to finish
    :return: the heuristic
    """
    heuristic = 0
    if not is_endgame:
        pawns_w = board.pieces(chess.PAWN, chess.WHITE)
        pawns_b = board.pieces(chess.PAWN, chess.BLACK)
        for i in pawns_w:
            heuristic += psq_tables_w[chess.PAWN][i]
        for i in pawns_b:
            heuristic -= psq_tables_b[chess.PAWN][i]

        knights_w = board.pieces(chess.KNIGHT, chess.WHITE)
        knights_b = board.pieces(chess.KNIGHT, chess.BLACK)
        for i in knights_w:
            heuristic += psq_tables_w[chess.KNIGHT][i]
        for i in knights_b:
            heuristic -= psq_tables_b[chess.KNIGHT][i]
    return heuristic


def castling(board: chess.Board, color: bool) -> int:
    """
    Function that calculate the heristic value of castlings right
    :param board: chess.Board to ponder
    :param color: the color of the player to ponder
    :return: the score
    """
    score = 0
    score += 40 if board.has_kingside_castling_rights(color) else 0
    score += 40 if board.has_queenside_castling_rights(color) else 0
    return score


def materiel_mob(board):
    """
    Function to calculate the mobility and material score
    :param board: board to calculate
    :return: the score
    """
    score = 0
    score -= material(board, False)
    score += material(board, True)
    score -= mobility(board, False) * 20
    score += mobility(board, True) * 20
    return score


def evaluate(board):
    """
    Function that is the entry point. it evaluates a board.
    it return negative number if is black advantage or positive for white
    :param board: the board to eval
    :return: the score of the board
    """
    score = 0
    score += materiel_mob(board)
    score += castling(board, True)
    score -= castling(board, True)
    score += game_over(board)
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
