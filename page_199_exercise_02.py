"""
Author: Nguyen Duc Thang
Date: 24/10/2021
Program: page_199_exercise_02.py
Problem: Write the code for a filtering that generates a list of the positive numbers in a list
    named numbers. You should use a lambda to create the auxiliary function.
Solution:


"""
numbers = [1,2,3,4,5,6,-7,-8,-9]
print("Number:\n ",numbers)
print("Cac so duong: ")
for pos_nums in numbers:
   if pos_nums > 0:
      print(pos_nums, end = " ")