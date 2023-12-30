def invert(lst):
    for i in lst:
        if int(i) > 0:
            i *= -1
        else:
            i *= 1
    return lst

a = input()
print(invert(a))