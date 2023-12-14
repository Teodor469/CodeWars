def reverse_middle(lst):
    middle = len(lst) // 2
    if len(lst) > 4:
        middle_part = lst[middle-1:middle+2][::-1]
    elif len(lst) == 4:
        middle_part = lst[middle-1:middle+1][::-1]
    left_part = lst[:middle-1]
    right_part = lst[middle+2:]

    return left_part + middle_part + right_part

lst = input()
print(reverse_middle(lst))