def distinct(seq):
    new_list = []
    for item in seq:
        if item not in new_list:
            new_list.append(item)
    return new_list
