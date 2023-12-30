def filter_list(lst):
    new_list = []
    
    for item in lst:
        if isinstance(item, int):
            new_list.append(item)
    
    return new_list

a = input()
print(filter_list(a))