import chess
import random
import sys

import IA.alpha_beta as ab
import IA.min_max as mm
import IA.evaluation as ev


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
    sys.exit("\033[93m" + "ERREUR : Il faut l'argument suivant en paramètre : (1) - IA/IA  (2) - Joueur/IA" + "\033[0m")

# Récupération du paramètre entré par le joueur.
argument = int(sys.argv[1])

# Sélection de la difficulté de l'intelligence artificielle.
profondeur = int(input("Quelle est la difficulté de l'intelligence artificielle (Profondeur) : "))

# Sélection de l'algorithme utilisé par l'intelligence artificielle.
algoModeGame = int(
    input("Choisissez l'algorithme utilisé pour l'intelligence artificielle (min_max (0) / alpha_beta (1)) : "))

# Initialisation de l'échiquier.
board = chess.Board()
# Définition du nombre de coups joués.
count = 1
# Définition de la priorité de jeu pour le joueur ou l'intelligence artificielle,
# définie de manière aléatoire afin de déterminer le premier joueur.
joueurIA = random.randint(1, 2)
# Affichage de l'échiquier initial.
print(board)

# Définition de la boucle de jeu.
while not board.is_game_over():

    # Entrez dans le mode de jeu IA/IA.
    if argument == 1:

        # Exécution du mode de jeu correspondant : Algorithme alpha_beta
        if algoModeGame == 1:
            board.push(ab.best_play(board, board.turn, profondeur))
            print(
                "----------------------------------------------------------------------------------------------------")
            print("Nombre de coups actuels : ", count, "Score : ", ev.evaluer(board), "Profondeur : ", profondeur,
                  "Algorithme : alpha_beta")
            print(
                "----------------------------------------------------------------------------------------------------")
            print(board)
            count += 1

        # Exécution du mode de jeu correspondant : Algorithme min_max
        elif algoModeGame == 0:
            board.push(mm.best_play(board, board.turn, profondeur))
            print("-------------------------------------------------------------------------------------------------")
            print("Nombre de coups actuels : ", count, "Score : ", ev.evaluer(board), "Profondeur : ", profondeur,
                  "Algorithme : min_max")
            print("--------------------------------------------------------------------------------------------------")
            print(board)
            count += 1

    # Entrez dans le mode de jeu Joueur/IA.
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
                print("Nombre de coups actuels : ", count, "Score : ", ev.evaluer(board), "Profondeur : ", profondeur,
                      "Algorithme : alpha_beta")
                print("---------------------------------------------------------------------------------------------")
                print(board)
                count += 1

            # Exécution du mode de jeu correspondant : Algorithme min_max
            elif algoModeGame == 0:
                board.push(mm.best_play(board, board.turn, profondeur))
                print("---------------------------------------------------------------------------------------------")
                print("Nombre de coups actuels : ", count, "Score : ", ev.evaluer(board), "Profondeur : ", profondeur,
                      "Algorithme : min_max")
                print("---------------------------------------------------------------------------------------------")
                print(board)
                count += 1

            # Passage de la main de jeu au joueur.
            joueurIA = 1

# Affichage du motif de fin de partie
motif_fin(board)
