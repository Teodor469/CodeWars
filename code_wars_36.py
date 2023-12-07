def gimme_the_letters(sp):
    start, end = sp.split('-')
    result = ''

    start_ascii, end_ascii = ord(start), ord(end)

    # Build the string using a loop
    for ascii_value in range(start_ascii, end_ascii + 1):
        result += chr(ascii_value)

    return result
