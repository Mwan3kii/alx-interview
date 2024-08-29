#!/usr/bin/python3
"""A program that solves n queens problem"""
import sys


def print_board(board, n):
    """Print positions of queen on board"""
    solution = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                solution.append([i, j])
    print(solution)


def is_safe(board, i, j, r):
    """Checks if placing queen at row column is safe"""
    return board[i] in (j, j - i + r, i - r + j)


def solve_nqueens(board, row, n):
    """Solves n queens problem using backtracking"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if is_safe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                solve_nqueens(board, row + 1, n)


def create_board(size):
    """Generates the board with empty colunms"""
    return [0 * size for i in range(size)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(n)
    solve_nqueens(board, 0, n)
