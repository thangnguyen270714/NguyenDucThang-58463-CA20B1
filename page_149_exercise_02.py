"""
Author: Nguyen Duc Thang
Date: 11/10/2021
Program: page_149_exercise_02.py
Problem:Define a function named even. This function expects a number as an argument and
    returns True if the number is divisible by 2, or it returns False otherwise. (Hint: A
    number is evenly divisible by 2 if the remainder is 0.)
Solution:

"""
a=float(input('Hay nhap so:'))
def even(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(even(a))