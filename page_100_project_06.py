"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_100_project_06.py
Problem:The German mathematician Gottfried Leibniz developed the following method to approximate the value of π:
    π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
    Write a program that allows the user to specify the number of iterations used in
    this approximation and that displays the resulting value.
Solution:
    ....
"""
lanlap = int(input("Hay nhap so lan lap: "))
a = 0
b = 1
sign = True
for i in range(lanlap):
    a = a + 1 / b if sign else a - 1 / b
    b += 2
    sign = not sign
pi = a * 4
print('pi=',pi)