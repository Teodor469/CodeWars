def find_it(seq) -> str:

    count_dict = {}
    for num in seq:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count % 2 == 1:
            return num
    
a = input()
print(find_it(a))
