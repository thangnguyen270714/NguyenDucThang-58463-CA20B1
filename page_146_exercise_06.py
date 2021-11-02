"""
Author: Nguyen Duc Thang
Date: 10/10/2021
Program: page_146_exercise_06.py
Problem: Write a loop that replaces each number in a list named data with its absolute value.
Solution:

"""
data=[-4,2,-3,-1,5]
a = []
for count in data:
    if count < 0:
        a.append(abs(count))
    else:
        a.append(count)
print("Gia tri tuyet doi data:\n", a)