import chess

import IA.alpha_beta_trans as ia
from util.funcs import *


def go(board: chess.Board, args: []):
    profondeur = 4
    n_pieces = total_pieces(board)
    if n_pieces < 15:
        profondeur += 1
        if n_pieces < 10:
            profondeur += 1
            if n_pieces < 5:
                profondeur += 2
    if len(args) > 1:
        for i in range(len(args)):
            if args[i] == "depth":
                profondeur = int(args[i + 1])
    best_move: chess.Move = ia.best_play(board, board.turn, profondeur)
    print("bestmove ", best_move.uci())


def uci(name, author, ok: bool):
    print("id name ", name)
    print("id author ", author)
    if ok:
        print("uciok")


def position(board: chess.Board, args: str):
    if args[0] == "fen":
        board.set_fen(args[1])
    if args[0] == "startpos":
        board.set_fen(board.starting_fen)
        if len(args) > 1:
            if args[1] == "moves":
                board.reset()
                for m in args[2:]:
                    board.push_uci(m)
