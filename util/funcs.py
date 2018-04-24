import random

import chess
import collections


def creative_move(fifo: collections.deque) -> chess.Move:
    """
    Function hat return and random move between moves in the dequeu, for
    the computer not playing always the same. It choose a random move that is at least
    bestmove - epsilon dist.
    :param fifo: a deque with [(move, evaluation)] it is already sorted
    :return:
    """
    epsilon = 30  # the gap
    best_eval = fifo[0][1]  # getting the best eval 0 best move 1 eval

    # Creating a list with move with epsilon difference with the best move
    moves = [move_eval for move_eval in fifo if best_eval - epsilon <= move_eval[1] and move_eval[0] != 0]


    print(moves)
    return random.choice(moves)[0]


def number_pieces(board: chess.Board, color) -> int:
    """
    Function that return the number of pieces on the board for a player
    :param board: the ches board
    :param color: the color of the player chess.WHITE or chess.BLACK
    :return: number of pieces
    """
    num = 0
    num += board.pieces(chess.PAWN, color).__len__()
    num += board.pieces(chess.KNIGHT, color).__len__()
    num += board.pieces(chess.BISHOP, color).__len__()
    num += board.pieces(chess.ROOK, color).__len__()
    num += board.pieces(chess.QUEEN, color).__len__()
    return num


def total_pieces(board: chess.Board) -> int:
    """
    Function that return the total of pieces on the board
    :param board: the chess board
    :return: number of pieces
    """
    return number_pieces(board, chess.WHITE) + number_pieces(board, chess.BLACK)


def game_over_reason(board: chess.Board):
    """
    Function that will print the result and the reason of the endgame
    :param board: board to analyse
    """
    print("Game over:", end="")
    if board.is_fivefold_repetition():
        print("fivefold repetition")
    if board.is_seventyfive_moves():
        print("70 moves")
    if board.is_stalemate():
        print("Pat")
    if board.is_checkmate():
        print("Check mate")
    print("result: ", board.result())
