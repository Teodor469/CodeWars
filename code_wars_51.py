def triangle(row):
    while len(row) > 1:  # Continue until the final row is generated
        new_row = ""
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:  # If the colors are identical, use the same color
                new_row += row[i]
            else:  # If the colors are different, use the missing color
                if "R" not in (row[i], row[i + 1]):
                    new_row += "R"
                elif "G" not in (row[i], row[i + 1]):
                    new_row += "G"
                elif "B" not in (row[i], row[i + 1]):
                    new_row += "B"
        row = new_row  # Update the row for the next iteration

    return row  # Return the final color

a = int(input())
print(triangle(a))