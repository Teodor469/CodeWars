def count_sheep(n):
    murmur = ""
    for i in range(1, n + 1):
        murmur += f"{i} sheep..."
    return murmur

n = int(input())
print(count_sheep(n))