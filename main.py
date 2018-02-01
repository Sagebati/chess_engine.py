import chess
import chess.uci
import IA.MinMax as mm

engine = chess.uci.popen_engine("stockfish-8-linux/Linux/stockfish_8_x64")
engine.uci()
print(engine.name)
print(engine.author)

engine.isready()
engine.ucinewgame()
board = chess.Board()

while not board.is_checkmate():
    #(move, dontknow) = engine.go()
    #board.push_uci(move.__str__())
    #engine.position(board.fen())
    board.push_uci(mm.bestPlay(board, 2).uci())
    #engine.position(board.fen())
    print(board)

