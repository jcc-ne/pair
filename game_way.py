import numpy as np
from scipy.misc import comb
import itertools


def factorial_recur(n):
    if n == 0:
        return 1
    return factorial_recur(n - 1) * n


def way(m, n):
    """
        m: number of space
        n: number of move
    """
    return factorial_recur(n) / (factorial_recur(m) * factorial_recur(n - m))


def way_scipy(m, n):
    return comb(n, m)


def way_recursive(n, m, steps=[], count=0):
    """
    recursive version of way(n, m)
        m: number of space
        n: number of move
    """
    if n == 0:
        if m == sum(steps):
            count += 1
        return count

    count = way(n-1, m, steps + [1], count)
    count = way(n-1, m, steps + [0], count)
    return count


def way_simulation(m, n):
    """
    simulation version of way(n, m)
        m: number of space
        n: number of move
        return: True means success
    """
#     moves = np.random.randint(2, size=n)
    dic_game = {}
    for game in range(10000):
        game_move, result = one_game(m, n)
        dic_game[game_move] = result
    return dic_game


def one_game(m, n):
    moves = []
    for i in range(0, n):
        choice = np.random.randint(2)
        moves.append(choice)

    if m == sum(moves):
        return (tuple(moves), True)
    return (tuple(moves), False)


for i in itertools.product(range(2), repeat=5):
    print i


def count(N, M):
    if (M == 0):
        return 1
    elif N == 0:
        return 0
    elif N == M:
        return 1
    return count(N-1, M-1) + count(N-1, M)
