def odd_or_even(arr):
    sum_of_array = sum(arr)
    if sum_of_array % 2 == 1:
        return "odd"
    return "even"