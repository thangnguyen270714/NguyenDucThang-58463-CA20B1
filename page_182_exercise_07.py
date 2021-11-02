"""
Author: Nguyen Duc Thang
Date: 24/10/2021
Program: page_182_exercise_07.py
Problem: Explain what happens when the following recursive function is called with the
    values "hello" and 0 as arguments:

    def example(aString, index):
        if index == len(aString):
            return ""
        else:
            return aString[index] + example(aString, index + 1)
Solution:

"""

def example(aString, index):
    if index == len(aString):
        return ""
    else:
        return aString[index] + example(aString, index + 1)