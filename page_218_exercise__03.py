"""
Author: Nguyen Duc Thang
Date: 19/10/2021
Program:Add a function named circle to the polygons module. This function expects the
same arguments as the square and hexagon functions. The function should draw a
circle. (Hint: the loop iterates 360 times.)
Solution:
    ....
"""
def circle(t, length):
    for count in range(360):
        t.forward(length)
        t.left(90)
