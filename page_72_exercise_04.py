"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_72_exercise_04.py
Problem: Write a loop that outputs the numbers in a list named salaries. The outputs should be
formatted in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:
    ....
"""
a=float(input('Nhap so tien luong:'))
print('%12s'% ('Tien luong'))
for tien in range(6):
    print('%12.2f'% (a))


