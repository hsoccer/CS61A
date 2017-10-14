from hog import *

lst_ave = []
lst_idx = []

for i, j, k, l in [[1, 6, 4, 4], [2, 4, 5, 5], [3, 4, 0, 4], [4, 5, 4, 6], [4, 9, 3, 6], [5, 3, 4, 4], [5, 4, 2, 5], [5, 4, 5, 0], [5, 6, 3, 5], [6, 4, 6, 6], [6, 6, 7, 6], [6, 7, 4, 6], [9, 3, 2, 5]]:
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
    if ave_win > 0.735:
        print('strategy({}, {}, {}, {}) win rate:'.format(i, j, k, l), ave_win)
        lst_ave.append(ave_win)
        lst_idx.append([i, j, k, l])

print(lst_ave)
print(lst_idx)
