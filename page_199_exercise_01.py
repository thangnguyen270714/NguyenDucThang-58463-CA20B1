"""
Author: Nguyen Duc Thang
Date: 24/10/2021
Program: page_199_exercise_01.py
Problem:Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.
Solution:

"""
number = [1,2,3,4,5,-6,-7,-8,-9]
print("Number: " + str(number))
res = list(map(abs, number))
print("So tuyet doi : " + str(res))