"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_118_exercise_01.py
Problem:Assume that the variable data refers to the string "Python rules!". Use a string method from Table 4-2 to perform the following tasks:
    a. Obtain a list of the words in the string.
    b. Convert the string to uppercase.
    c. Locate the position of the string "rules".
    d. Replace the exclamation point with a question mark.
Solution:

    ....
"""
a= "Python rules!"
#a. Obtain a list of the words in the string.
print(a.center(12))
#b. Convert the string to uppercase.
print(a.upper())
#c. Locate the position of the string "rules".
print(a.find("rules"))
#d. Replace the exclamation point with a question mark.
print(a.replace('!', '?'))
