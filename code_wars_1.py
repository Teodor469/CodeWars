def grow(arr):
    result = 1  # Initialize the result to 1

    for number in arr:
        result *= number  # Multiply the current number with the result

    return result