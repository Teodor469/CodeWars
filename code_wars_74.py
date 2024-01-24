def rot13(message):
    result = []
    for char in message:
        if char.isalpha():
            if char.islower():
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            else:
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

mssg = "test"
print(rot13(mssg))
