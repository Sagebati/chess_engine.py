import chess

debug=False

def gui_to_engine(command):
    if command == "uci":
        return False
    if command == "debug on":
        debug = True

    if command == "debug off":
        debug = False

    if command == "isready":
        print("readyok")
    if command == "ucinewgame":
        return chess.Board()
    if command == "position":



# TODO azdaz
def engine_to_gui():
    return False