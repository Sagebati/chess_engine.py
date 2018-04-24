import chess

import eval.evaluation as ev
import ia.min_max as ab


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


board = chess.Board()
print(board)

count = 1
profondeur = 2

# print("2 Games modes: 1: ia vs ia ; 2: ia vs You")
# resp1 = input("Which mode ?")
# resp2 = input("Which difficulty for ia 1 ?")
# resp3 = ""
# if int(resp1) == 1:
#     resp3 = input("Which difficulty for ia 2 ?")

while not board.is_game_over():
    board.push(ab.best_play(board, board.turn, profondeur))
    print("---------------------------------")
    print("nbrcoups", count, "score:", ev.evaluate(board), "profondeur:", profondeur)
    print("---------------------------------")
    print(board)
    count += 1

motif_fin(board)
