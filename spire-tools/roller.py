import random


def roll(dice):
    """Rolls a dice number of d10s, keeps the best one, and returns the dice pool for display and the text result."""
    pool = [random.randint(1, 10) for die in range(dice)]
    best = max(pool)
    if best == 1:
        res = "Critical failure. Fail, and take double stress."
    elif best in range(1, 6):
        res = "Failure. Fail, and take stess."
    elif best in range(6, 8):
        res = "Success at a cost. Succeed, but take stress."
    elif best in range(8, 10):
        res = "Success. Succeed, and take no stress."
    elif best == 10:
        res = "Critical Success. Succeed dramatically, and increase outgoing stress dice by 1 step."
    return pool, res
