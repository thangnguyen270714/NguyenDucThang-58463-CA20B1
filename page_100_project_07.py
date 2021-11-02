"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_100_project_07.py
Problem:Teachers in most school districts are paid on a schedule that provides a salary
    based on their number of years of teaching experience. For example, a beginning
    teacher in the Lexington School District might be paid $30,000 the first year. For
    each year of experience after this first year, up to 10 years, the teacher receives a
    2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district.
    The inputs are the starting salary, the percentage increase, and the number of years in the schedule. Each row
    in the schedule should contain the year number and the salary for that year
Solution:
    ....
"""
mucluong = int(input("Hay nhap mua luong cua ban: "))
phantram = (float(input("So phan tram tang sau moi nam: ")) / 100)
sonam = int(input("So nam cong tac cua ban: "))
for i in range(1,sonam+1):
    print("{} nam cong tac:{:0.2f}".format(i , mucluong * ((1 + phantram) ** (i - 1))))