import numpy as np


def pn(c):
    return c // 5 + 1

def pnd(c):
    t = 0
    for i in np.arange(0,c//10+1):
        t += pn(c-10*i)
    return t

def pndq(c):
    t = 0
    for i in np.arange(0,c//25+1):
        t += pnd(c-25*i)
    return t


def arbcoins(c,t=[25, 10, 5, 1]):
    count = 0
    t.sort(reverse=True)

    if len(t) < 2:
        if(c < t[0]):
            return 0
        return int(c % t[0] == 0)

    for v in t:
        t.remove(v)
        print v
        for i in np.arange(0,c//v+1):
            count += arbcoins(c - v*i, t)

    return count

# ---- from joel's solu


def arbcoins_mod(c,t=[25, 10, 5, 1]):
    count = 0
    t.sort(reverse=True)

    if len(t) < 2:
        if(c < t[0]):
            return 0
        return 1

    for i in np.arange(0,c//t[0]+1):
        count += arbcoins_mod(c - t[0]*i, t[1:])

    return count

# ---- from joel's solu


def ways1(cents, coins=[25, 10, 5, 1]):
    sum = 0
    for i in range(cents//coins[0]+1):
        for j in range((cents-i*coins[0])//coins[1]+1):
            for k in range((cents-i*coins[0]-coins[1])//coins[2]+1):
                sum += 1
    return sum

def ways2(cents, coins=[25, 10, 5, 1]):
    sum = 0
    if len(coins) == 1:
        return 1
    for i in range(cents//coins[0] + 1):
        sum += ways2(cents - i * coins[0], coins[1:])
    return sum

def ways3(cents, coins=[25, 10, 5, 1]):
    if cents < 0 or not coins:
        return 0
    if cents == 0:
        return 1
    return ways3(cents - coins[0], coins) + ways3(cents, coins[1:])

def ways4(cents, coins=[25, 10, 5, 1]):
    pass

def ways5(cents, coins=[25, 10, 5, 1]):
    nb_combinations = [1] + [0] * cents
    for coin in coins:
        print nb_combinations
        print "coin: ", coin
        print "cents + 1: ", cents + 1
#         for sub_case in
    return nb_combinations[cents]
