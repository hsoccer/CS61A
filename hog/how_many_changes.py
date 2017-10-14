from hog import *

six = 0
four = 0

for i in range(100000):
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False # Whether 4-sided dice have been swapped for 6-sided
    score0, score1 = 0, 0
    goal = 100
    # BEGIN PROBLEM 6
    "*** REPLACE THIS LINE ***"
    while score0 < goal and score1 < goal:
        if player == 0:
            num_rolls = always_roll(4)(score0, score1)
            add = take_turn(num_rolls, score1, select_dice(dice_swapped))
            score0 += add
            if is_perfect_piggy(add):
                dice_swapped = 1 - dice_swapped
            if is_swap(score0, score1):
                score0, score1 = score1, score0
            player = other(player)
            if select_dice(dice_swapped) == six_sided:
                six += 1
            else:
                four += 1
        else:
            num_rolls = always_roll(4)(score1, score0)
            add = take_turn(num_rolls, score0, select_dice(dice_swapped))
            score1 += add
            if is_perfect_piggy(add):
                dice_swapped = 1 - dice_swapped
            if is_swap(score1, score0):
                score0, score1 = score1, score0
            player = other(player)
            if select_dice(dice_swapped) == six_sided:
                six += 1
            else:
                four += 1

print(2 * six / (six + four), 2 * four / (six + four))
        # END PROBLEM 6
