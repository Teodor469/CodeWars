def hamming_weight(x):
    converted = bin(x)[2:]
    return converted.count("1")

x = int(input())
print(hamming_weight(x))