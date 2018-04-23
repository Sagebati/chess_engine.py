import random

import chess
import collections


def creative_move(fifo: collections.deque):
    """
    Function hat return and random move between moves in the dequeu
    :param fifo:
    :return:
    """
    epsilon = 0.3
    best_eval = fifo[0][1]

    # Creating a list with move with 0.5 difference with the best move
    coup_possibles = [coupeval for coupeval in fifo if best_eval - epsilon <= coupeval[1] <= best_eval + epsilon]

    return random.choice(coup_possibles)[0]


def number_pieces(board: chess.Board, color):
    num = 0
    num += board.pieces(chess.PAWN, color).__len__()
    num += board.pieces(chess.KNIGHT, color).__len__()
    num += board.pieces(chess.BISHOP, color).__len__()
    num += board.pieces(chess.ROOK, color).__len__()
    num += board.pieces(chess.QUEEN, color).__len__()
    return num


def total_pieces(board: chess.Board):
    return number_pieces(board, chess.WHITE) + number_pieces(board, chess.BLACK)
