"""
Author: Nguyen Duc Thang
Date: 25/09/2021
Program: page_125_exercise_05.py
Problem: Write a code segment that prompts the user for a filename. If the file exists, the
    program should print its contents on the terminal. Otherwise, it should print an error message
Solution:

    ....
"""
import os.path
ten = input("Nhap ten thu muc: ")
if os.path.exists(ten):
    thumuc = open(ten, 'r')
    print(thumuc.read())
else:
    print("Loi: Khong tim thay thuc muc!")


