def square_digits(num):
    result = ''
    for n in str(num):
        sq = int(n) ** 2
        result += str(sq)
    return int(result)

        