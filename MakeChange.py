"""Make change given the fewest amount of coins."""


Coins = {25, 10, 5, 1}


def make_change(amount):
    """Make change given the fewest amount of coins."""
    coin_count = 0
    while amount > 0:
        if amount >= 25:
            amount -= 25
            coin_count += 1
            continue
        if amount < 25 and amount > 10:
            amount -= 10
            coin_count += 1
            continue
        if amount < 10 and amount > 5:
            amount -= 5
            coin_count += 1
            continue
        # Handle pennies here
        amount -= 1
        coin_count += 1
    return coin_count

assert(make_change(25) == 1)
assert(make_change(36) == 3)
assert(make_change(4) == 4)
assert(make_change(72) == 6)
