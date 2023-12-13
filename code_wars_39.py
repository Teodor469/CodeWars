def good_vs_evil(good, evil):
    worth_good = [1, 2, 3, 3, 4, 10]
    worth_evil = [1, 2, 2, 2, 3, 5, 10]

    sum_good = sum(int(count) * worth for count, worth in zip(good.split(), worth_good))
    sum_evil = sum(int(count) * worth for count, worth in zip(evil.split(), worth_evil))

    if sum_good > sum_evil:
        return "Battle Result: Good triumphs over Evil"
    elif sum_evil > sum_good:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
