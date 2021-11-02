"""
Author: Nguyen Duc Thang
Date: 11/10/2021
Program: page_166_project_07.py
Problem:Write a program that inputs a text file. The program should print the unique
    words in the file in alphabetical order
Solution:

"""
# Nhap tep text07.txt
file_input = input("Hay nhap tep: ")
with open (file_input,'r') as f:
    fp=f.read().split()
fp=set(fp)
fp=sorted(fp)
print(fp)
print("Number of unique word: {0}".format(len(fp)))