

# How many ways can you get “heads” on 5 flips of a coin?
#
# What is the probability of getting 3 ‘heads’ on 5 flips of a fair coin?
#
# You flip a fair coin 100 times.  What is the probability that you get 30 heads?
#
# An urn has 5 red balls and 15 blue.  You draw up 5 from the urn and put them
# in a new urn.
#  -  How many ways are there of drawing 5 red balls (and no blue?)
#  -  4 red balls and 1 blue?

5C4 * 15C1 = 15 * 5 = 75

#  -  2 red balls and 3 blue?

5C2 * 15C3 = 4550
#
# A deck of cards has 52 cards in it, 4 of which are aces.  Suppose you draw
# one card, then, without replacing it in the deck, draw another card.
# Then, again without replacing either the first or second, you draw a third
# card.  What is the probability that exactly two of the sampled cards will be aces?

from fraction import Fraction
from scipy.misc import comb

def nCr(n, r):
    return int(reduce(lambda x, y: x* y, (Fraction(n-i, i+1) for i in range(r))))


# binomial distribution
# C(trials, n) p ^ n (1-p) ^ (trials - n)
