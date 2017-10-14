from hog import *
import numpy as np

table = [[0 for i in range(100)] for j in range(100)]

for score in range(100):
    print(score)
    for opponent_score in range(100):
        max_ave = 0
        max_rolls = 0
        for num_rolls in range(11):
            six_sum = 0
            four_sum = 0
            for i in range(10000):
                new_score = score + take_turn(num_rolls, opponent_score, six_sided)
                if is_swap(new_score, opponent_score):
                    new_score = opponent_score
                if new_score == (opponent_score + 1) * 2:
                    new_score = new_score * 0.391297 + opponent_score * 0.608703
                if new_score == (opponent_score + 8) * 2:
                    new_score = new_score * 0.997511 + opponent_score * 0.002489
                if new_score == (opponent_score + 9) * 2:
                    new_score = new_score * 0.990041 + opponent_score * 0.009959
                if new_score == (opponent_score + 10) * 2:
                    new_score = new_score * 0.975023 + opponent_score * 0.024977
                if new_score == (opponent_score + 12) * 2:
                    new_score = new_score * 0.947235 + opponent_score * 0.052765
                if new_score == (opponent_score + 13) * 2:
                    new_score = new_score * 0.958411 + opponent_score * 0.041589
                if new_score == (opponent_score + 14) * 2:
                    new_score = new_score * 0.954958 + opponent_score * 0.045042
                if new_score == (opponent_score + 15) * 2:
                    new_score = new_score * 0.963603 + opponent_score * 0.036397
                if new_score == (opponent_score + 16) * 2:
                    new_score = new_score * 0.968353 + opponent_score * 0.031647
                if new_score == (opponent_score + 17) * 2:
                    new_score = new_score * 0.947207 + opponent_score * 0.052793
                if new_score == (opponent_score + 18) * 2:
                    new_score = new_score * 0.976532 + opponent_score * 0.023468
                if new_score == (opponent_score + 19) * 2:
                    new_score = new_score * 0.972340 + opponent_score * 0.027660
                if new_score == (opponent_score + 20) * 2:
                    new_score = new_score * 0.987810 + opponent_score * 0.012190
                if new_score == (opponent_score + 21) * 2:
                    new_score = new_score * 0.993066 + opponent_score * 0.006934
                if new_score == (opponent_score + 22) * 2:
                    new_score = new_score * 0.996539 + opponent_score * 0.003461
                if new_score == (opponent_score + 23) * 2:
                    new_score = new_score * 0.981726 + opponent_score * 0.018274
                if new_score == (opponent_score + 24) * 2:
                    new_score = new_score * 0.999649 + opponent_score * 0.000351
                if new_score == (opponent_score + 29) * 2:
                    new_score = new_score * 0.998699 + opponent_score * 0.001301
                six_sum += new_score
                new_score = score + take_turn(num_rolls, opponent_score, four_sided)
                if is_swap(new_score, opponent_score):
                    new_score = opponent_score
                if new_score == (opponent_score + 1) * 2:
                    new_score = new_score * 0.391297 + opponent_score * 0.608703
                if new_score == (opponent_score + 8) * 2:
                    new_score = new_score * 0.997511 + opponent_score * 0.002489
                if new_score == (opponent_score + 9) * 2:
                    new_score = new_score * 0.990041 + opponent_score * 0.009959
                if new_score == (opponent_score + 10) * 2:
                    new_score = new_score * 0.975023 + opponent_score * 0.024977
                if new_score == (opponent_score + 12) * 2:
                    new_score = new_score * 0.947235 + opponent_score * 0.052765
                if new_score == (opponent_score + 13) * 2:
                    new_score = new_score * 0.958411 + opponent_score * 0.041589
                if new_score == (opponent_score + 14) * 2:
                    new_score = new_score * 0.954958 + opponent_score * 0.045042
                if new_score == (opponent_score + 15) * 2:
                    new_score = new_score * 0.963603 + opponent_score * 0.036397
                if new_score == (opponent_score + 16) * 2:
                    new_score = new_score * 0.968353 + opponent_score * 0.031647
                if new_score == (opponent_score + 17) * 2:
                    new_score = new_score * 0.947207 + opponent_score * 0.052793
                if new_score == (opponent_score + 18) * 2:
                    new_score = new_score * 0.976532 + opponent_score * 0.023468
                if new_score == (opponent_score + 19) * 2:
                    new_score = new_score * 0.972340 + opponent_score * 0.027660
                if new_score == (opponent_score + 20) * 2:
                    new_score = new_score * 0.987810 + opponent_score * 0.012190
                if new_score == (opponent_score + 21) * 2:
                    new_score = new_score * 0.993066 + opponent_score * 0.006934
                if new_score == (opponent_score + 22) * 2:
                    new_score = new_score * 0.996539 + opponent_score * 0.003461
                if new_score == (opponent_score + 23) * 2:
                    new_score = new_score * 0.981726 + opponent_score * 0.018274
                if new_score == (opponent_score + 24) * 2:
                    new_score = new_score * 0.999649 + opponent_score * 0.000351
                if new_score == (opponent_score + 29) * 2:
                    new_score = new_score * 0.998699 + opponent_score * 0.001301
                four_sum += new_score
            ave = (six_sum * 0.935 + four_sum * 1.065) / 20000
            if max_ave < ave:
                max_ave = ave
                max_rolls = num_rolls
        table[score][opponent_score] = max_rolls
print(table)
