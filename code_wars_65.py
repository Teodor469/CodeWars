def find_average(numbers):
    if not numbers:
        return 0

    average = sum(numbers) / len(numbers)
    return average