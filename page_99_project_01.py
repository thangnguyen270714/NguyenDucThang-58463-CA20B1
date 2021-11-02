"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_99_project_01.py
Problem: Write a program that accepts the lengths of three sides of a triangle as inputs.
    The program output should indicate whether or not the triangle is an equilateral triangle.
Solution:
    ....
"""
a=float(input('Nhap canh a='))
b=float(input('Nhap canh b='))
c=float(input('Nhap canh c='))
if a==b and a==c:
    print('Tam giac can')
else:
    print('Khong phai tam giac can')


