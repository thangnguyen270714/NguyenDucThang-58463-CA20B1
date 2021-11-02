"""
Author: Nguyen Duc Thang
Date: 02/09/2021
Program: page_46_exercise_04.py
Problem: What happens when the print function prints a string literal with embedded
newline characters?
Solution:
    When you evaluate a string in the Python shell without the print function, you can see the
literal for the newline character, \n, embedded in the result, as follow
The newline character \n is called an escape sequence. Escape sequences are the way
Python expresses special characters, such as the tab, the newline, and the backspace (delete
key), as literals

    ....
"""
print("ho va ten: Nguyen Duc Thang")
print("ho va ten:\nNguyen Duc Thang")

