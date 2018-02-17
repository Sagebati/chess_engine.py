import chess
import IA.min_max as mm
import IA.alpha_beta as ab
import IA.evaluation as ev

board = chess.Board()

count = 0
profondeur = 4
while not board.is_checkmate():
    # (move, dontknow) = engine.go()
    # board.push_uci(move.__str__())
    # engine.position(board.fen())
    # engine.position(board.fen())
    print("---------------------------------")
    print("nbrcoups", count, "score:", ev.evaluer(board), "profondeur:",profondeur)
    print("---------------------------------")
    print(board)
    board.push(ab.best_play(board, board.turn, profondeur))
    count += 1
