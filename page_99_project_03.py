"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_99_project_03.py
Problem:Modify the guessing-game program of Section 3.5 so that the user thinks of a
    number that the computer must guess. The computer must make no more than
    the minimum number of guesses, and it must prevent the user from cheating by
    entering misleading hints.
    (Hint: Use the math.log function to compute the minimum number of guesses needed after the lower and upper bounds are entered.)
Solution:
    ....
"""
import random
sonho = int(input("Hay nhap so nho: "))
solon = int(input("Hay nhap so lon: "))
solan=int(input('Hay nhap gioi han so lan doan:'))
so = random.randint(sonho,solon)
count=0
while True:
    sodoan = int(input("Hay nhap so du doan: "))
    count += 1
    if solan==count:
        print('Ban da het luot du doan\nChuc ban may man lan sau!')
        break
    elif sodoan < so:
        print("Qua nho!")
    elif sodoan > so:
        print("Qua lon!")
    elif sodoan==so:
        print("Ban da doan chinh xác sau",count,"lan thu!")
        break
