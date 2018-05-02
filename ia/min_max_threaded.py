import math
import multiprocessing as mp

import chess

import eval.evaluation as ev


def _min(board, profondeur):
    """
    :param board: le tableau du jeu
    :type board: chess.Board
    :param profondeur: profondeur de l'algo
    :type profondeur: int
    """
    if profondeur == 0 or board.is_game_over():
        return ev.evaluate(board)

    val = math.inf
    for play in board.legal_moves:
        board.push(play)
        val = min(val, _max(board, profondeur - 1))
        board.pop()

    return val


def _max(board, profondeur):
    """
    :param board: le tableau du jeu
    :type board: chess.Board
    :param profondeur: profondeur de l'algo
    :type profondeur: int
    """
    if profondeur == 0 or board.is_game_over():
        return ev.evaluate(board)

    val = -math.inf

    for play in board.legal_moves:
        board.push(play)
        val = max(val, _min(board, profondeur - 1))
        board.pop()
    return val


def best_play(board: chess.Board, player, profondeur=5):
    """
    :param profondeur: profondeur de l'algorithme
    :param board: chess.Board
    :param player: boolean
    :return: chess.Move
    """
    results = []
    id = 0
    moves = []
    pool = mp.Pool(processes=16)
    for move in board.legal_moves:
        moves.append(move)
        clone = board.copy(stack=False)
        clone.push(move)
        if player:
            results.append((pool.apply(_min, args=(clone, profondeur)), id))
        else:
            results.append((pool.apply(_max, args=(clone, profondeur)), id))
        id += 1
    if player:
        m = max(results)
    else:
        m = min(results)

    return moves[m[1]]
