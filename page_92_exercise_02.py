"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_92_exercise_02.py
Problem: The factorial of an integer N is the product of the integers between 1 and N, inclusive.
    Write a while loop that computes the factorial of a given integer N.
Solution:
    ....
"""
x=int(input('Nhap giai thua cua so:'))
y=1
z=1
while y<=x:
    z *= y
    y += 1
print('Giai thua =',z)






