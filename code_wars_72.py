def abbrev_name(name):
    u = name.split()
    a = u[0][0].upper()
    b = u[1][0].upper()
    
    return f"{a}.{b}"

print(abbrev_name("Harry Petterson"))