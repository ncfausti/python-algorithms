"""
Find the greatest difference between list items.

Given a list, return the largest difference between
individual items.
"""


def max_difference(ls):
    """Return the greatest difference between any two list items."""
    low = ls[0]
    high = ls[0]
    for item in ls:
        if item < low:
            low = item
        if item > high:
            high = item
    return (high - low)

assert(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9)
assert(max_difference([5, 2, 5, 3, 4, 5, 6, 7, 7, 8, 9]) == 7)
assert(max_difference([0, 2, 3, 4, 5, 6, 7, 800, 9, 10]) == 800)


def max_sale(ls):
    """
    Return the indices that provide the greatest sale price.

    For index i, return the max of index (i - j), where j is an index
    of a number that came before i.
    """
    pass
