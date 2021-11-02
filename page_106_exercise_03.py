"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_106_exercise_03.py
Problem: Assume that the variable myString refers to a string. Write a code segment that
    uses a loop to print the characters of the string in reverse order.
Solution:
    ....
"""
text=str(input('Nhap ky tu:'))
for i in range(len(text)):
    print(i,text[i])