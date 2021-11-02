"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_72_exercise_02.py
Problem: Write a code segment that displays the values of the integers x, y, and z on a single
    line, such that each value is right-justified with a field width of 6.
Solution:
    ....
"""
x=int(input('Hay nhap gia tri x:'))
y=int(input('Hay nhap gia tri y:'))
z=int(input('Hay nhap gia tri z:'))
print('%6s%6s%6s' % ('x','y','z'))
print('%6s%6s%6s' % (x , y , z))



