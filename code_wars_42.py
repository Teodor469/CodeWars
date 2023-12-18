def multiply(num):
    if num == 0:
        return 0

    sign = -1 if num < 0 else 1
    absolute_num = abs(num)
    power = len(str(absolute_num))

    return sign * absolute_num * (5 ** power)