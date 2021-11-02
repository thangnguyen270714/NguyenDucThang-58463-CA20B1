"""
Author: Nguyen Duc Thang
Date: 25/09/2021
Program: page_125_exercise_02.py
Problem: Write a code segment that opens a file for input and prints the number of
four-letter words in the file
Solution:

    ....
"""
count=0
f = open("myfile.txt", 'r')
for i in f:
    ds=i.split()
    for n in ds:
        count+=1
print('So luong tu co 4 chu la:',count,'tu')