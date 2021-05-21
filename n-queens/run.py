import fire
from typing import *

from dataclasses import dataclass, field
import numpy as np


def place_queen(board, i, j) -> np.array:
    board = board.copy()
    board[i, j] = 1
    for ii in range(board.shape[0]):
        if board[ii, j] == 0:
            board[ii, j] = -1
    for jj in range(board.shape[1]):
        if board[i, jj] == 0:
            board[i, jj] = -1

    def _is_valid(i_, j_):
        return (
            0 <= i_ < board.shape[0]
            and
            0 <= j_ < board.shape[1]
        )


    # Diagonals
    for dd in range(1, board.shape[0]):
        if _is_valid(i+dd, j+dd):
            if board[i+dd, j+dd] == 0:
                board[i+dd, j+dd] = -1

        if _is_valid(i+dd, j-dd):
            if board[i+dd, j-dd] == 0:
                board[i+dd, j-dd] = -1

        if _is_valid(i-dd, j-dd):
            if board[i-dd, j-dd] == 0:
                board[i-dd, j-dd] = -1

        if _is_valid(i-dd, j+dd):
            if board[i-dd, j+dd] == 0:
                board[i-dd, j+dd] = -1

    return board


def place_n_queens(board, i, n):
    if n == 0:
        return [board]

    if i >= board.shape[0]:
        return []

    solved_boards = []

    for ii in range(i, board.shape[0]):
        for jj in range(0, board.shape[1]):
            if board[ii, jj] == 0:
                board2 = place_queen(board, ii, jj)
                new_solutions = place_n_queens(board2, ii+1, n-1)
                solved_boards.extend(new_solutions)

    return solved_boards


def print_board(board):
    print('\n')
    for i in range(board.shape[0]):
        ln = []
        for j in range(board.shape[1]):
            if board[i, j] == 1:
                ln.append('Q')
            else:
                ln.append('.')
        print(''.join(ln))


def run(n: int):
    print(f'n: {n}')

    board = np.zeros(shape=(n, n), dtype=np.int32)

    solns = []
    placed = 0

    solved_boards = place_n_queens(board, 0, n)

    for b in solved_boards:
        print_board(b)

if __name__ == '__main__':
    fire.Fire(run)

