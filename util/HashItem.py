import chess


class Hashentry:
    def __init__(self, zobrist: int, depth: int, flag: int, evaluation: int, ancient: int, move: chess.Move):
        """
        :param zobrist: the zobrist hash
        :param depth: depth of the search 0 if leaf 1 if before last
        :param flag:
        :param evaluation: evaluation of the board
        :param ancient:
        :param move:
        """
        self.zobrist = zobrist
        self.depth = depth
        self.flag = flag
        self.evaluation = evaluation
        self.ancient = ancient
        self.move = move
