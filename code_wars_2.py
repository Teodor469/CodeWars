def sale_hotdogs(n):
    # your code here

    if n < 5:
        price = 100
    elif  n >= 5 and n < 10:
        price = 95
    elif n >= 10:
        price = 90
    return n * price

