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
    """
    min_price = ls[0]
    max_sale = ls[1] - ls[0]

    for i in range(1, len(ls)):
        min_price = min(min_price, ls[i - 1])
        current_sale = ls[i] - min_price
        max_sale = max(current_sale, max_sale)
    return max_sale


assert(max_sale([5, 2, 5, 3, 4, 5, 6, 7, 7, 8, 9]) == 7)
assert(max_sale([5, 2, 5, 3, 4, 5, 60, 7, 7, 8, 9]) == 58)
assert(max_sale([9, 7, 4, 3, 1]) == -1)
assert(max_sale([9, 7, 4, 2, 1]) == -1)
