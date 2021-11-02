"""
Author: Nguyen Duc Thang
Date: 25/10/2021
Program: page_204_project_09.py
Problem: Write a program that computes and prints the average of the numbers in a text
    file. You should make use of two higher-order functions to simplify the design.
Solution:

"""

from functools import reduce
# Enter file test.txt
filename = input("Enter the input file name: ")
inputfile=open(filename, 'r')

#Read the numbers as strings into a list
lyst = []
for line in inputfile:
    lyst.extend(line.split())

#Conver all the strings in the list to numbera
lyst = list(map(float, lyst))

#Compute the sum of the numbers
sum = reduce(lambda x,y: x+y, lyst)

#Print the average
if len(lyst) == 0:
    average = 0
else:
    average = sum/len(lyst)
print("The average is: ", average)