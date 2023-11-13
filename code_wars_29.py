def reverse_seq(n):
    pass


def generate_array(n):
    array = []
    for i in range(n, 0, -1):
        array.append(i)
    return array

n = 5
result = generate_array(n)
print(result)