"""
Author: Nguyen Duc Thang
Date: 10/10/2021
Program: page_146_exercise_04.py
Problem:Write a loop that accumulates the sum of the numbers in a list named data.
Solution:

"""
data=[3,4,5,6,7]
sum=0
for count in range(len(data)):
    sum = data[count] + sum
print(sum)
