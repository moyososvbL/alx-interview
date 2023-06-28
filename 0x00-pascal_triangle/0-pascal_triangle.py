#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []  # Return an empty list if n <= 0

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1

        for j in range(1, i):
            # Calculate each element of the row as the sum of the two elements from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle  # Return the generated triangle


# Example usage
print(pascal_triangle(5))
