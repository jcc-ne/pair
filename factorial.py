import numpy as np


def factorial(n):
    a = np.arange(1, n + 1)
    return a.prod()


def factorial_while(n):
    m = n
    while n > 1:
        m *= (n - 1)
        n -= 1
    return m


def factorial_recur(n):
    if n == 0:
        return 1
    return factorial_recur(n - 1) * n


def fib(n):
    l = [0, 1]
    for i in l:
        l.append(l[-1] + l[-2])
        if len(l) > n - 1:
            break
    return l


def fib_recur(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fib_recur(n - 1) + fib_recur(n - 2))

known = {0: 0, 1: 1}


def fib_memo(n):
    if n in known:
        return known[n]
    res = fib_memo(n-1) + fib_memo(n-2)
    known[n] = res
    return res
