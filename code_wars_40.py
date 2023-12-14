def reverse_middle(lst):
    middle = len(lst) // 2
    middle_part = lst[middle-1:middle+2][::-1]
    left_part = lst[:middle-1]
    right_part = lst[middle+2:]

    return left_part + middle_part + right_part
