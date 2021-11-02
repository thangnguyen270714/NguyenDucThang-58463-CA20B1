"""
Author: Nguyen Duc Thang
Date: 25/09/2021
Program: page_125_exercise_03.py
Problem: Assume that a file contains integers separated by newlines. Write a code segment
    that opens the file and prints the average value of the integers.
Solution:

    ....
"""
count = 0
sum = 0
inputFile = open("myfile1.txt",'r')
for line in inputFile:
    line=line.strip()
    sum = sum + int(line)
    count += 1
    if count == 0:
        average = 0
    else:
        average = sum /count
print("The average is", (round(average,2)))