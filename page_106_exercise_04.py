"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_106_exercise_04.py
Problem: Assume that the variable myString refers to a string, and the variable
    reversedString refers to an empty string. Write a loop that adds the characters
    from myString to reversedString in reverse order.
Solution:
    ....
"""
mystring=input('Nhap ky tu:')
reversedString=''
for i in range (len(mystring)):
    reversedString=mystring[i]
    print('reversedString:',reversedString)
