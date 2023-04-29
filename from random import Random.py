from random import Random
from itertools import combinations

# When using random numbers, hardcode the seed to make results reproducible.

rng = Random(12345)

# Define the suits and ranks that a deck of playing cards is made of.

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

deck = [(rank, suit) for suit in suits for rank in ranks]


def deal_hand(n, taken=None):
    """Deal a random hand with n cards, without replacement."""
    result, taken = [], taken if taken else []
    while len(result) < n:
        c = rng.choice(deck)
        if c not in result and c not in taken:
            result.append(c)
    return result

