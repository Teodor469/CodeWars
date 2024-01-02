def binary_array_to_number(arr):
    binary_string = ''.join(map(str, arr))
    decimal_value = int(binary_string, 2)
    return decimal_value

a = input()
print(binary_array_to_number(a))