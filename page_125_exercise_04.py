"""
Author: Nguyen Duc Thang
Date: 25/09/2021
Program: page_125_exercise_04.py
Problem: Write a code segment that prints the names of all of the items in the current working directory
Solution:

    ....
"""
import os
currentDirectoryPath = os.getcwd()
list = os.listdir(currentDirectoryPath)
for name in list:
    if "." in name:
        print(name)
