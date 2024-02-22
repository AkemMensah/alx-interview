#!/usr/bin/python3
"""Solving N Queens with Backtracing"""
import sys


def nqueens(n, y, board):
    """
    Method: nqueens - place n queens
            on an n by n board so that
            no queens are attacking any
            others.
    Parameters: n is an int that sets
                board size and # of queens
    Return: All possible solutions to
            placement, in list of lists form
    """
    for x in range(n):
        hold = 0
        for q in board:
            if x == q[1]:
                hold = 1
                break
            if y - x == q[0] - q[1]:
                hold = 1
                break
            if x - q[1] == q[0] - y:
                hold = 1
                break
        if hold == 0:
            board.append([y, x])
            if y != n - 1:
                nqueens(n, y + 1, board)
            else:
                print(board)
            del board[-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n, 0, [])

if __name__ == '__main__':
    main()
