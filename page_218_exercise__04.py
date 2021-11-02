"""
Author: Nguyen Duc Thang
Date: 19/10/2021
Program:The functions that draw polygons in the polygons module have the same pattern, varying
only in the number of sides (iterations of the loop). Factor this pattern into a more general
function named polygon, which takes the number of sides as an additional argument.
Solution:
    ....
"""

def pentagon(t, length):
    for count in range(5):
        t.forward(length)
        t.left(60)

