def find_short(s):
    words = s.split()
    lengths = [len(word) for word in words] 
    return min(lengths)

a = input()
print(find_short(a))