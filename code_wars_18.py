def count_sheeps(sheep):
    count = 0  # Initialize a count to 0
    
    # Iterate through the list
    for is_present in sheep:
        if is_present:  # Check if the sheep is True (present)
            count += 1  # Increment the count
    
    return count  # Return the final count

