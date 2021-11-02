"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_92_exercise_03.py
Problem: The log 2 of a given number N is given by M in the equation N 5 2M. Using integer
    arithmetic, the value of M is approximately equal to the number of times N can be
    evenly divided by 2 until it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N.
    You can check your code by importing the math.log function and evaluating the expression round(math.log(N, 2)) (note
    that the math.log function returns a floating-point value).
Solution:
    ....
"""
import math
x=int(input('Hay nhap so N:'))
n=0
while True:
    n+=1
    x=x/2
    if x==0:
        break
print('gia tri M=',n)












