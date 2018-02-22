import chess
import IA.min_max_threaded as ab
import IA.evaluation as ev

board = chess.Board()
print(board)

count = 0
profondeur = 3


def motif_fin(board: chess.Board):
    print("motif de fin:", end="")
    if board.is_fivefold_repetition():
        print("repitition 5 fois")
    if board.is_seventyfive_moves():
        print("Règle des 70 coups")
    if board.is_stalemate():
        print("Pat")
    if board.is_checkmate():
        print("Echec est mat")
    print("resultat:", board.result())


while not board.is_game_over():
    # (move, dontknow) = engine.go()
    # board.push_uci(move.__str__())
    # engine.position(board.fen())
    # engine.position(board.fen())
    print("---------------------------------")
    print("nbrcoups", count, "score:", ev.evaluer(board), "profondeur:", profondeur)
    print("---------------------------------")
    board.push(ab.best_play(board, board.turn, profondeur - 1))
    print(board)
    count += 1

motif_fin(board)
