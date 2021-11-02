"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_101_project_09.py
Problem:Write a program that receives a series of numbers from the user and allows the
    user to press the enter key to indicate that he or she is finished providing inputs.
    After the user presses the enter key, the program should print the sum of the numbers and their average
Solution:
    ....
"""
theSum = 0.0
n=-1
while True:
    n += 1
    data = input("Enter a number or just enter to quit: ")

    if data == "":
        break
    number = float(data)
    theSum += number
print("The sum is", theSum)
x=float(theSum)
a=x/n
print('The average is',a)

