"""
Author: Nguyen Duc Thang
Date: 11/10/2021
Program: page_149_exercise_04.py
Problem:Define a function named summation. This function expects two numbers, named
    low and high, as arguments. The function computes and returns the sum of the
    numbers between low and high, inclusive.
Solution:

"""
sothap = int(input("Nhap so thap: "))
socao = int(input("Nhap so cao: "))
tong = 0
for count in range(sothap, socao + 1):
    tong = tong + count
print(tong)