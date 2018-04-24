#!/bin/python
import sys

import chess

import uci.gui_eng as ge

"""
UCI ENGINE
"""

def split_comm_args(inp: str):
    strss = inp.split(" ")
    if len(strss) > 1:
        return strss[0], strss[1:]
    else:
        return strss[0], None


name = "Quetzal"
author = "Samuel Batissou, Bejamin Cohen"

debug = False
board = chess.Board()
while 1:

    inp = input()
    command, args = split_comm_args(inp)

    if command == "uci":
        ge.uci(name, author, True)
    if command == "debug on":
        debug = True
    if command == "debug off":
        debug = False
    if command == "isready":
        print("readyok")
    if command == "ucinewgame":
        board = chess.Board()
    if command == "position":
        ge.position(board, args)
    if command == "go":
        ge.go(board, args)
    if command == "quit":
        sys.exit(0)
