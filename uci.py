
debug=False




def gui_to_engine(command:str):
    if command == "uci":

    if command == "debug on":
        debug = True

    if command == "debug off":
        debug = False

    if command == "isready":
        print("readyok")



def engine_to_gui():