def array_manip(array):
    new_array = [-1] * len(array)
    for i in range(len(array)):
        least_greater = float('inf')
        for j in range(i + 1, len(array)):
            if array[j] > array[i] and array[j] < least_greater:
                least_greater = array[j]
        if least_greater != float('inf'):
            new_array[i] = least_greater
    return new_array