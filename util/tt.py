import chess
import chess.polyglot as zb


def findboardorbdd(board: chess.Board, tt: {}, depth, alphabeta, ev=None):
    h = zb.zobrist_hash(board)
    if h in tt.keys():
        return True, tt[h]
    else:
        tt[h] = HashItem(h, depth, ev, alphabeta)
        return False, None


class HashItem:
    def __init__(self, zobrist: int, depth: int, evaluation: int, alphabeta: tuple):
        """
        :param zobrist: the zobrist hash
        :param depth: depth of the search 0 if leaf 1 if before last
        :param flag:
        :param evaluation: evaluation of the board
        :param ancient:
        :param best_move:
        """
        self.zobrist = zobrist
        self.depth = depth
        self.alphabeta = alphabeta
        # self.flag
        self.evaluation = evaluation
        # self.best_move = best_move
        # self.ancient
