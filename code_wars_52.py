def sort_array(source_array):
    sorted_odd_numbers = []

    # Extract odd numbers from the array and sort them
    for number in source_array:
        if number % 2 == 1:
            sorted_odd_numbers.append(number)

    sorted_odd_numbers.sort()

    result = []
    for number in source_array:
        if number % 2 == 1:
            result.append(sorted_odd_numbers.pop(0))
        else:
            result.append(number)

    return result

a = input()
print(sort_array(a))