import chess


class HashItem:
    def __init__(self, zobrist: int, depth: int,  evaluation: int,  best_move: chess.Move):
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
        #self.flag
        self.evaluation = evaluation
        self.best_move = best_move
        #self.ancient
