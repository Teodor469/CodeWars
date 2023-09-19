def opposite(number):
    if number > 0:
        return -number
    elif number < 0:  # Changed the condition here from 'number == 0' to 'number < 0'
        return abs(number)  # Return the absolute value of the negative number
    else:
        return 0  # Return 0 for the case when the number is 0