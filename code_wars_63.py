def positive_sum(arr):
    positive = []
    for n in arr:
        if n > 0:
            positive.append(n)
    return sum(positive)

arr = [1, -4, 7, 12]
result = positive_sum(arr)
print(result)