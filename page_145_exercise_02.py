"""
Author: Nguyen Duc Thang
Date: 10/10/2021
Program: page_145_exercise_02.py
Problem:Assume that the variable data refers to the list [5, 3, 7]. Write the expressions
that perform the following tasks:
    a. Replace the value at position 0 in data with that value’s negation.
    b. Add the value 10 to the end of data.
    c. Insert the value 22 at position 2 in data.
    d. Remove the value at position 1 in data.
    e. Add the values in the list newData to the end of data.
    f. Locate the index of the value 7 in data, safely.
    g. Sort the values in data.
Solution:


"""
data=[5,3,7]
#a. Replace the value at position 0 in data with that value’s negation.
print(data[0])
#b. Add the value 10 to the end of data.
data[2]=10
print(data)
#c. Insert the value 22 at position 2 in data.
data[2]=27
print(data)
#d. Remove the value at position 1 in data.
data.pop(1)
print(data)
#e. Add the values in the list newData to the end of data.
newdata=[2,3,4]
b=data+newdata
print(b)
#f. Locate the index of the value 7 in data, safely.
a=7 in data
print(a)
#g. Sort the values in data.
b.sort()
print(b)


