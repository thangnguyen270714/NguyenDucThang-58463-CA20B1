"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_92_exercise_01.py
Problem: Translate the following for loops to equivalent while loops:
    a. for count in range(100):
    print(count)
    b. for count in range(1, 101):
    print(count)
    c. for count in range(100, 0, –1):
    print(count)
Solution:
    ....
"""
#a. for count in range(100):
a=0
while a<=100:
    a+=1
print(a)
# b. for count in range(1, 101):
theSum = 0
count = 1
while count <= 101:
    theSum += count
    count += 1
print(theSum)
#c for count in range(100, 0, -1):
x = 100
while x >= 1:
    x -= 1
    print(x,end=' ')





