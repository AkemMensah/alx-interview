#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. This program solves the N queens problem.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Utility function to solve N queens problem
    """
    # Base case: if all queens are placed
    if col >= n:
        queens_positions = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        solutions.append(queens_positions)
        return

    # Consider this column and try placing this queen i all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens_util(board, col + 1, n, solutions)

            # Backtrack: If placing queen in board[i][col] doesn't
            # lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0


def solve_nqueens(n):
    """
    Main function to solve N queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
