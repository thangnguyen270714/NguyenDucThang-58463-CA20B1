"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_70_exercise_05.py
Problem: Assume that the variable teststring refers to a string. Write a loop that prints
each character in this string, followed by its ASCII value.
Solution:
    ....
"""
a=str(input('Hay nhap ky tu ASCII:'))
b=ord(a)
for kytu in range(b, 128):
    print('\nKy tu ASCII:',kytu,end='')


