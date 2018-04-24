import chess

import eval.evaluation as ev
import ia.alpha_beta_tt as ab
from util.funcs import game_over_reason

board = chess.Board()

count = 0
depth = 1

while not board.is_game_over():
    print("---------------------------------")
    print("nbrcoups", count, "score:", ev.evaluate(board), "profondeur:", depth)
    print("---------------------------------")
    print(board)
    move = ab.best_play(board, board.turn, depth)
    if move == 0:
        print("bug")
    board.push(move)
    count += 1

game_over_reason(board)
