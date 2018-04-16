import chess

import IA.alpha_beta as ab
import IA.min_max as mm
import IA.evaluation as ev


# Sélection de la difficulté de l'intelligence artificielle.
profondeur = int(input("Quelle est la difficulté de l'intelligence artificielle (Profondeur) : "))

# Sélection de l'algorithme utilisé par l'intelligence artificielle.
algoModeGame = int(input("Choisissez l'algorithme utilisé pour l'intelligence artificielle (min_max (0) / alpha_beta (1)) : "))


# Initialisation de l'échiquier.
board = chess.Board()
# Définition  du nombre de coups joués.
count = 1

# Affichage de l'échiquier initial.
print(board)


# Définition de la boucle de jeu.
while not board.is_game_over():

    # Exécution du mode de jeu correspondant : Algorithmeal pha_beta
    if algoModeGame == 1 :
        board.push(ab.best_play(board, board.turn, profondeur))
        print("---------------------------------------------------------------------------------------")
        print("Nombre de coups actuels", count, "Score:", ev.evaluer(board), "Profondeur:", profondeur, "Algorithme : alpha_beta")
        print("---------------------------------------------------------------------------------------")
        print(board)
        count += 1

    # Exécution du mode de jeu correspondant : Algorithmeal min_max
    elif algoModeGame == 0:
        board.push(mm.best_play(board, board.turn, profondeur))
        print("--------------------------------------------------------------------------------------")
        print("Nombre de coups actuels", count, "Score:", ev.evaluer(board), "Profondeur:", profondeur, "Algorithme : min_max")
        print("--------------------------------------------------------------------------------------")
        print(board)
        count += 1


# Fsonction permettant l'affichage du motif de fin de partie.
def motif_fin(board: chess.Board):
    
    print("motif de fin:", end="")

    if board.is_fivefold_repetition():
        print("repitition 5 fois")
    elif board.is_seventyfive_moves():
        print("Règle des 70 coups")
    elif board.is_stalemate():
        print("Pat")
    elif board.is_checkmate():
        print("Echec est mat")

    print("resultat:", board.result())







