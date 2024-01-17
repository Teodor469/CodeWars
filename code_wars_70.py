def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0

arr = [6, 2, 1, 8, 10]
print(sum_array(arr))