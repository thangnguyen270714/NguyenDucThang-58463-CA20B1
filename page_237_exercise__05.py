"""
Author: Nguyen Duc Thang
Date: 19/10/2021
Program: How would a column-major traversal of a grid work? Write a code segment that
prints the positions visited by a column-major traversal of a 2-by-3 grid.
Solution:
    ....
"""
width = 2
height = 3
for y in range(height):
    for x in range(width):
        print((x, y), end = " ")