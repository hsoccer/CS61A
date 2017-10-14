from hog import *

M = 0

i_lst = [2, 2, 2, 3, 3, 4, 5, 5, 5]
j_lst = [5, 6, 8, 3, 9, 6, 3, 4, 5]
k_lst = [6, 5, 8, 9, 5, 4, 5, 4, 5]
l_lst = [9, 6, 7, 8, 4, 6, 0, 3, 8]

lst_ave = []
lst_idx = []

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                def strategy(score, opponent_score):
                    get = free_bacon(opponent_score)
                    if is_prime(get):
                        get = next_prime(get)
                    if (score + get) * 2 == opponent_score:
                        return 0
                    if get >= 8 and score + get != opponent_score * 2:
                        return 0
                    if score >= opponent_score * 2: ### score is very strong
                        return always_roll(i)(score, opponent_score)
                    if opponent_score * 2 >= score >= opponent_score: ### score is strong
                        return always_roll(j)(score, opponent_score)
                    if opponent_score >= score * 2: ### opp is very strong
                        return always_roll(k)(score, opponent_score)
                    if opponent_score >= score: ### opp is strong
                        return always_roll(l)(score, opponent_score)
                    return always_roll(4)(score, opponent_score)
                                    
                ave_win = average_win_rate(strategy)
                if ave_win > 0.75:
                    print('strategy({}, {}, {}, {}) win rate:'.format(i, j, k, l), ave_win)
                    lst_ave.append(ave_win)
                    lst_idx.append([i, j, k, l])

print(M)
print(lst_ave)
print(lst_idx)
