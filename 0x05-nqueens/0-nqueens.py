#!/usr/bin/python3
"""a module to implement the N queens puzzle is the
    challenge of placing N non-attacking queens on an N×N chessboard
"""

import sys


def user_input():
    """gets user input"""
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    else:
        n = sys.argv[1]
        if not n.isdecimal():
            print('N must be a number')
            sys.exit(1)
        elif int(n) < 4:
            print('N must be at least 4')
            sys.exit(1)
        else:
            return int(n)


def nqueens(n: int):
    """the function to solve the nqueens problem"""
    col = set()
    posD = set()
    negD = set()

    board = [[0] * n for i in range(n)]

    def backtracking(r):
        if r == n:
            res = [[r, c] for r, x in enumerate(board)
                   for c in x if board[r][c] == 1]
            print(res)
            return
        for c in range(n):
            if c in col or (r + c) in posD or (r - c) in negD:
                continue

            col.add(c)
            posD.add(r + c)
            negD.add(r - c)
            board[r][c] = 1
            backtracking(r + 1)

            col.remove(c)
            posD.remove(r + c)
            negD.remove(r - c)
            board[r][c] = 0
    backtracking(0)


n = user_input()

nqueens(n)
