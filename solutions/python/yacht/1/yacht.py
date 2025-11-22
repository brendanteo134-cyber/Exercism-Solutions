YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
COUNTABLE = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]
def score(dice, category):
    dice = sorted(dice)
    result = 0
    max_occurrences = max(dice, key=dice.count)
    min_occurrences = min(dice, key=dice.count)
    if category in COUNTABLE:
        result = dice.count(category) * category
    if category is LITTLE_STRAIGHT:
        if dice == [1, 2, 3, 4, 5]:
            result = 30
    if category is BIG_STRAIGHT:
        if dice == [2, 3, 4, 5, 6]:
            result = 30
    if category is CHOICE:
        result = sum(dice)
    if category is FULL_HOUSE:
        if dice.count(max_occurrences) == 3 and dice.count(min_occurrences) == 2:
            result = sum(dice)
    if category is FOUR_OF_A_KIND:
        if dice.count(max_occurrences) >= 4:
            result = max_occurrences * 4
    if category is YACHT:
        if dice.count(5) == len(dice):
            result = 50
    
    return result