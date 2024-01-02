def xo(s):
    lower = s.lower()
    x = lower.count('x')
    o = lower.count('o')

    if x == o:
        return True
    
    elif x == 0 and o == 0:
        return True
    
    else:
        return False
    
a = input()
print(xo(a))