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


    sr.daemon = True
    sr.start()

    board = Board()

    while True:
        line = sr.get()
        if line == None:
            break

        line = line.rstrip('\n')

        if len(line) == 0:
            continue

        l('IN: %s' % line)

        parts = line.split(' ')

        if parts[0] == 'uci':
            send('id name Feeks')
            send('id author Folkert van Heusden <mail@vanheusden.com>')
            send('uciok')

        elif parts[0] == 'isready':
            send('readyok')

        elif parts[0] == 'ucinewgame':
            board = Board()
            cm_thread_stop()

        elif parts[0] == 'auto':
            t = wait_init_thread(t)
            cm_thread_stop()

            tt = 1000
            n_rnd = 4
            if len(parts) == 2:
                tt = float(parts[1])

            ab = Board()
            while not ab.is_checkmate():
                if n_rnd > 0:
                    m = random_move(ab)
                    n_rnd -= 1

                else:
                    m = calc_move(ab, tt, 999999)
                    m = m[1]

                if m == None:
                    break

                ab.push(m)
                print(m)

            print('done')

        elif parts[0] == 'perft':
            cm_thread_stop()

            depth = 4
            if len(parts) == 2:
                depth = int(parts[1])

            start = time.time()
            total = 0

            for m in board.get_move_list():
                board.push(m)
                cnt = perft(board, depth - 1)
                board.pop()

                print('%s: %d' % (m.uci(), cnt))

                total += cnt

            print('===========================')
            took = time.time() - start
            print('Total time (ms) : %d' % math.ceil(took * 1000.0))
            print('Nodes searched  : %d' % total)
            print('Nodes/second    : %d' % math.floor(total / took))

        elif parts[0] == 'position':
            is_moves = False
            nr = 1
            while nr < len(parts):
                if is_moves:
                    board.push_uci(parts[nr])

                elif parts[nr] == 'fen':
                    board = Board(' '.join(parts[nr + 1:]))
                    break

                elif parts[nr] == 'startpos':
                    board = Board()

                elif parts[nr] == 'moves':
                    is_moves = True

                else:
                    l('unknown: %s' % parts[nr])

                nr += 1

        elif parts[0] == 'go':
            t = wait_init_thread(t)
            if cm_thread_stop():
                l('stop pondering')

            movetime = None
            depth = None
            wtime = btime = None
            winc = binc = 0
            movestogo = None

            nr = 1
            while nr < len(parts):
                if parts[nr] == 'wtime':
                    wtime = int(parts[nr + 1])
                    nr += 1

                elif parts[nr] == 'btime':
                    btime = int(parts[nr + 1])
                    nr += 1

                elif parts[nr] == 'winc':
                    winc = int(parts[nr + 1])
                    nr += 1

                elif parts[nr] == 'binc':
                    binc = int(parts[nr + 1])
                    nr += 1

                elif parts[nr] == 'movetime':
                    movetime = int(parts[nr + 1])
                    nr += 1

                elif parts[nr] == 'movestogo':
                    movestogo = int(parts[nr + 1])
                    nr += 1

                elif parts[nr] == 'depth':
                    depth = int(parts[nr + 1])
                    nr += 1

                else:
                    l('unknown: %s' % parts[nr])

                nr += 1

            ###
            current_duration = movetime

            if current_duration:
                current_duration = float(current_duration) / 1000.0

            elif wtime and btime:
                ms = wtime
                time_inc = winc
                if not board.turn:
                    ms = btime
                    time_inc = binc

                ms /= 1000.0
                time_inc /= 1000.0

                if movestogo == None:
                    movestogo = 40 - board.fullmove_number
                    while movestogo < 0:
                        movestogo += 40

                current_duration = (ms + movestogo * time_inc) / (board.fullmove_number + 7);

                limit_duration = ms / 15.0
                if current_duration > limit_duration:
                    current_duration = limit_duration

                if current_duration == 0:
                    current_duration = 0.001

                l('mtg %d, ms %f, ti %f' % (movestogo, ms, time_inc))
            ###
            if current_duration:
                l('search for %f seconds' % current_duration)

            if depth == None:
                depth = 999

            cm_thread_start(board, current_duration, depth, False)

            line = None
            while cm_thread_check():
                line = sr.get(0.01)

                if line:
                    line = line.rstrip('\n')

                    if line == 'stop' or line == 'quit':
                        break

            result = cm_thread_stop()

            if line == 'quit':
                break

            if result and result[1]:
                send('bestmove %s' % result[1].uci())
                board.push(result[1])

            else:
                send('bestmove a1a1')

            if ponder and not board.is_game_over():
                send('info string start pondering')
                cm_thread_start(board.copy(), is_ponder=True)

        elif parts[0] == 'quit':
            break

        elif parts[0] == 'fen':
            send('%s' % board.fen())

        elif parts[0] == 'eval' or parts[0] == 'deval':
            moves = pc_to_list(board, [])

            depth = None
            if parts[0] == 'deval':
                t = wait_init_thread(t)
                depth = int(parts[1])
            elif len(parts) == 2:
                check_move = chess.Move.from_uci(parts[1])

            send('move\teval\tsort score')
            for m in moves:
                if not m.move == check_move:
                    continue

                board.push(m.move)

                if depth:
                    rc = calc_move(board, None, depth)
                    v = rc[0]
                    send('%s\t%d\t%d (%s)' % (m.move, v, m.score, rc[1]))

                else:
                    v = evaluate(board)
                    if board.turn == chess.BLACK:
                        v = -v
                    send('%s\t%d\t%d' % (m.move, v, m.score))

                board.pop()

        elif parts[0] == 'moves':
            send('%s' % [m.uci() for m in board.get_move_list()])

        elif parts[0] == 'smoves':
            moves = pc_to_list(board, [])
            send('%s' % [m.move.uci() for m in moves])

        elif parts[0] == 'trymovedepth':
            t = wait_init_thread(t)
            board.push(chess.Move.from_uci(parts[1]))
            send('%s' % calc_move(board, None, int(parts[2])))
            board.pop()

        elif parts[0] == 'probett':
            t = wait_init_thread(t)
            print(tt_lookup(board))

        else:
            l('unknown: %s' % parts[0])
            send('Unknown command')

            sys.stdout.flush()

    cm_thread_stop()

except KeyboardInterrupt as ki:
    l('ctrl+c pressed')
    cm_thread_stop()

except Exception as ex:
    l(str(ex))
l(traceback.format_exc())