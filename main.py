import sys
import time

import chess

import eval.evaluation as ev
import ia.alpha_beta as ab
import ia.min_max as mm
import ia.alpha_beta_tt as tt


# Fonction permettant l'affichage du motif de fin de partie.
def motif_fin(board: chess.Board):
    print("motif de fin:", end="")

    if board.is_fivefold_repetition():
        print("repitition 5 fois")
    elif board.is_seventyfive_moves():
        print("Règle des 70 coups")
    elif board.is_stalemate():
        print("Pat")
    elif board.is_checkmate():
        print("Echec et mat")

    print("resultat : ", board.result())


# Message correspondant aux différents paramètres nécessaires pour l'exécution du script Python.
if len(sys.argv) != 2:
    sys.exit("\033[93m" + "ERREUR : Il faut l'argument suivant en paramètre : (1) - ia/ia  (2) - Joueur/ia" + "\033[0m")

# Récupération du paramètre entré par le joueur.
argument = int(sys.argv[1])

# Paramètres correspondants au choix de jeu ia/ia de l'intelligence artificielle.
profondeurIA1 = 2
profondeurIA2 = 2
algorithmeIA1 = 1
algorithmeIA2 = 1

# Paramètres correspondants au choix de jeu Joueur/ia de l'intelligence artificielle.
profondeur = 2
algoModeGame = 1

# Entrez dans le mode de jeu ia/ia.
if argument == 1:

    # Sélection de la difficulté de l'intelligence artificielle.
    profondeurIA1 = int(input("Quelle est la difficulté de l'intelligence artificielle N°1 (Profondeur) : "))

    # Sélection de l'algorithme utilisé par l'intelligence artificielle.
    algorithmeIA1 = int(input(
        "Choisissez l'algorithme utilisé pour l'intelligence artificielle  N°1 (min_max (0) / alpha_beta (1) / ab_tt("
        "2) : "))

    # Sélection de la difficulté de l'intelligence artificielle.
    profondeurIA2 = int(input("Quelle est la difficulté de l'intelligence artificielle N°2 (Profondeur) : "))

    # Sélection de l'algorithme utilisé par l'intelligence artificielle.
    algorithmeIA2 = int(input(
        "Choisissez l'algorithme utilisé pour l'intelligence artificielle  N°2 (min_max (0) / alpha_beta (1) / ab_tt("
        "2) : "))



elif argument == 2:

    # Sélection de la difficulté de l'intelligence artificielle.
    profondeur = int(input("Quelle est la difficulté de l'intelligence artificielle (Profondeur) : "))

    # Sélection de l'algorithme utilisé par l'intelligence artificielle.
    algoModeGame = int(
        input(
            "Choisissez l'algorithme utilisé pour l'intelligence artificielle (min_max (0) / alpha_beta (1) / ab_tt(2) : "))

# Initialisation de l'échiquier.
board = chess.Board()
# Définition du nombre de coups joués.
count = 1
# Définition de la priorité de jeu pour le joueur ou l'intelligence artificielle,
joueurIA = 1

# Affichage de l'échiquier initial.
print("\n\n\nAffichage de l'échiquier initial")
print("--------------------------------")
print(board)
print("--------------------------------")

# Définition de la boucle de jeu.
while not board.is_game_over():

    # Entrez dans le mode de jeu ia/ia.
    if argument == 1:

        # Tour de jeu correspondant au joueur.
        if joueurIA == 1:

            # Exécution du mode de jeu correspondant : Algorithme alpha_beta
            if algorithmeIA1 == 1:
                board.push(ab.best_play(board, board.turn, profondeurIA1))
                print(
                    "\n----------------------------------------------------------------------------------------------------")
                print("+Joueur Actuel+")
                print("ia N°1 / Blanc", "Profondeur : ", profondeurIA1, "Algorithme : alpha_beta\n")
                print("+Joueur Adverse+")
                print("ia N°2 / Noir", "Profondeur : ", profondeurIA2)
                print("\nNombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "\n\n")
                print(board)
                print(
                    "----------------------------------------------------------------------------------------------------\n")
                count += 1

            # Exécution du mode de jeu correspondant : Algorithme min_max
            elif algorithmeIA1 == 0:
                board.push(mm.best_play(board, board.turn, profondeurIA1))
                print(
                    "\n-------------------------------------------------------------------------------------------------")
                print("+Joueur Actuel+")
                print("ia N°1 / Blanc", "Profondeur : ", profondeurIA1, "Algorithme : min_max\n")
                print("+Joueur Adverse+")
                print("ia N°2 / Noir", "Profondeur : ", profondeurIA2)
                print("\nNombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "\n\n")
                print(board)
                print(
                    "--------------------------------------------------------------------------------------------------\n")
                count += 1

            elif algorithmeIA1 == 2:
                board.push(tt.best_play(board, board.turn, profondeurIA1))
                print(
                    "\n-------------------------------------------------------------------------------------------------")
                print("+Joueur Actuel+")
                print("ia N°1 / Blanc", "Profondeur : ", profondeurIA1, "Algorithme : min_max\n")
                print("+Joueur Adverse+")
                print("ia N°2 / Noir", "Profondeur : ", profondeurIA2)
                print("\nNombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "\n\n")
                print(board)
                print(
                    "--------------------------------------------------------------------------------------------------\n")
                count += 1

            joueurIA = 2

        elif joueurIA == 2:

            # Exécution du mode de jeu correspondant : Algorithme alpha_beta
            if algorithmeIA2 == 1:
                board.push(ab.best_play(board, board.turn, profondeurIA2))
                print(
                    "\n----------------------------------------------------------------------------------------------------")
                print("+Joueur Actuel+")
                print("ia N°2 / Noir", "Profondeur : ", profondeurIA2, "Algorithme : alpha_beta\n")
                print("+Joueur Adverse+")
                print("ia N°1 / Blanc", "Profondeur : ", profondeurIA1)
                print("\nNombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "\n\n")
                print(board)
                print(
                    "----------------------------------------------------------------------------------------------------\n")
                count += 1

            # Exécution du mode de jeu correspondant : Algorithme min_max
            elif algorithmeIA2 == 0:
                board.push(mm.best_play(board, board.turn, profondeurIA2))
                print(
                    "\n----------------------------------------------------------------------------------------------------")
                print("+Joueur Actuel+")
                print("ia N°2 / Noir", "Profondeur : ", profondeurIA2, "Algorithme : min_max\n")
                print("+Joueur Adverse+")
                print("ia N°1 / Blanc", "Profondeur : ", profondeurIA1)
                print("\nNombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "\n\n")
                print(board)
                print(
                    "----------------------------------------------------------------------------------------------------\n")
                count += 1

            elif algorithmeIA2 == 2:
                board.push(tt.best_play(board, board.turn, profondeurIA2))
                print(
                    "\n----------------------------------------------------------------------------------------------------")
                print("+Joueur Actuel+")
                print("ia N°2 / Noir", "Profondeur : ", profondeurIA2, "Algorithme : Alpha_Beta_tt\n")
                print("+Joueur Adverse+")
                print("ia N°1 / Blanc", "Profondeur : ", profondeurIA1)
                print("\nNombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "\n\n")
                print(board)
                print(
                    "----------------------------------------------------------------------------------------------------\n")
                count += 1

            joueurIA = 1


    # Entrez dans le mode de jeu Joueur/ia.
    elif argument == 2:

        # Tour de jeu correspondant au joueur.
        if joueurIA == 1:

            # Initialement le coup est déclaré comme invalide pour le joueur.
            coupInvalide = False

            # Boucle permettant la répétition de la demande du coup du joueur temps que celui-ci est considéré comme
            # invalide.
            while coupInvalide is False:

                # Récupération du coup joueur.
                tmp = input("Quel est votre coup : ")

                try:
                    # Exécution du coup potentiel joueur.
                    board.push_san(tmp)
                    # Si aucune erreur est lancée le coup est déclaré comme valide.
                    coupInvalide = True
                except ValueError:
                    # Affichage d'un message permettant de signifier au joueur que le coup est invalide.
                    print("Coup invalide ( " + tmp + " ) merci de bien vouloir recommencer\n")
                    # Si une erreur est lancée le coup est déclaré comme invalide.
                    coupInvalide = False

            # Affichage de l'échiquier.
            print(board)
            # Passage de la main de jeu à l'intelligence artificielle.
            joueurIA = 2

        # Tour de jeu correspondant à l'intelligence artificielle.
        else:

            # Exécution du mode de jeu correspondant : Algorithme alpha_beta
            if algoModeGame == 1:
                board.push(ab.best_play(board, board.turn, profondeur))
                print("----------------------------------------------------------------------------------------------")
                print("Nombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "Profondeur : ", profondeur,
                      "Algorithme : alpha_beta")
                print("---------------------------------------------------------------------------------------------")
                print(board)
                count += 1

            # Exécution du mode de jeu correspondant : Algorithme min_max
            elif algoModeGame == 0:
                board.push(mm.best_play(board, board.turn, profondeur))
                print("---------------------------------------------------------------------------------------------")
                print("Nombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "Profondeur : ", profondeur,
                      "Algorithme : min_max")
                print("---------------------------------------------------------------------------------------------")
                print(board)
                count += 1

            elif algoModeGame == 2:
                # Passage de la main de jeu au joueur.
                board.push(tt.best_play(board, board.turn, profondeur))
                print("---------------------------------------------------------------------------------------------")
                print("Nombre de coups actuels : ", count, "Score : ", ev.evaluate(board), "Profondeur : ", profondeur,
                      "Algorithme : min_max")
                print("---------------------------------------------------------------------------------------------")
                print(board)
                count += 1
            joueurIA = 1

# Affichage du motif de fin de partie
motif_fin(board)
