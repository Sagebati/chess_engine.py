import chess
import IA.MinMax as Mm
import os
board = chess.Board()

count = 0
while not board.is_checkmate():
    # (move, dontknow) = engine.go()
    # board.push_uci(move.__str__())
    # engine.position(board.fen())
    board.push_uci(Mm.best_play(board, 1).uci())
    count += 1
    # engine.position(board.fen())
    print(board)
    os.system("clear")
    print("---------------------------------")
    print(count)
