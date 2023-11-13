def to_alternating_case(string):
    result = ""
    for letter in string:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result