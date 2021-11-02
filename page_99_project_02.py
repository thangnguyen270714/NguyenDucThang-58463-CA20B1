"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_99_project_02.py
Problem:Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is a right triangle.
    Recall from the Pythagorean theorem that in a right triangle, the square of
    one side equals the sum of the squares of the other two sides.
Solution:
    ....
"""
a=float(input('Nhap canh huyen cua tam giac:'))
b=float(input('Nhap canh b cua tam giac:'))
c=float(input('Nhap canh c cua tam giac:'))
if a**2==(b**2+c**2):
    print('Tam giac vuong')
else:
    print('Khong phai tam giac vuong')


