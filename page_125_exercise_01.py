"""
Author: Nguyen Duc Thang
Date: 25/09/2021
Program: page_125_exercise_01.py
Problem:. Write a code segment that opens a file named myfile.txt for input and prints the
    number of lines in the file
Solution:

    ....
"""
f = open("myfile.txt", 'r')
text = f.read()
print(text)
