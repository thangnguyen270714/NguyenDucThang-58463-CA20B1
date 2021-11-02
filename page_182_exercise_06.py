"""
Author: Nguyen Duc Thang
Date: 24/10/2021
Program: page_182_exercise_06.py
Problem: Explain what happens when the following recursive function is called with the
    values "hello" and 0 as arguments:

    def example(aString, index):
        if index < len(aString):
            example(aString, index + 1)
            print(aString[index], end = "")
Solution:


"""
def example(aString, index):
    if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end="")