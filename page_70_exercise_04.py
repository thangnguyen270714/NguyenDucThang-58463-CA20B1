"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_70_exercise_04.py
Problem: Write a loop that prints the first 128 ASCII values followed by the corresponding
    characters (see the section on characters in Chapter 2). Be aware that most of the
    ASCII values in the range “0..31” belong to special control characters with no standard print representation, so you might see strange symbols in the output for these
    values.
Solution:
    ....
"""
a=int(input('Nhạp ky tu ASCII:'))
for kytu in range(a, 128):
    print('\nKy tu ASCII:',chr(kytu),end='')









