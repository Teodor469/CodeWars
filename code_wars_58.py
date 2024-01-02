def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
    

a = input()
print(sum_two_smallest_numbers(a))