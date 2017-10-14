from hog import *
import random

lst = [0 for i in range(30)]

for i in range(1000000):
    l = random.choices((4, 6), weights=[11, 9], k=1)
    if l == [4]:
        dice = select_dice(True)
    else:
        dice = select_dice(False)
    sum_dice = roll_dice(4, dice)
    if is_prime(sum_dice):
        sum_dice = next_prime(sum_dice)
    lst[sum_dice] += 1

print(lst)
