"""
Author: Nguyen Duc Thang
Date: 10/10/2021
Program: page_146_exercise_05.py
Problem:Assume that data refers to a list of numbers, and result refers to an empty list.
    Write a loop that adds the nonzero values in data to the result list, keeping them
    in their relative positions and excluding the zeros.
Solution:

"""
data = [0,2,1,5,2,3]
a = ""
for count in data:
   if count != 0:
       a += str(count)
print(a)