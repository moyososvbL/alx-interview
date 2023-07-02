#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    row = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle


n = int(input("Enter the value of n: "))
result = pascal_triangle(n)

expected_result = [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]

if result == expected_result:
    print("Output matches expected result.")
else:
    print("Output does not match expected result.")
