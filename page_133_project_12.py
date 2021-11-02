"""
Author: Nguyen Duc Thang
Date: 26/09/2021
Program: page_133_project_012.py
Problem:The Payroll Department keeps a list of employee information for each pay period
    in a text file. The format of each line of the file is the following:
    <last name> <hourly wage> <hours worked>
    Write a program that inputs a filename from the user and prints to the terminal a
    report of the wages paid to the employees for the given period. The report should
    be in tabular format with the appropriate header. Each line should contain an
    employee’s name, the hours worked, and the wages paid for that period
Solution:
    Nhap file tienluong.txt
    ....
"""
# file tienluong.txt
file_name =open(input('Enter input file name: '))

# print the header on terminal
print('\n%-15s%-10s%-10s' % ('Name', 'Hours', 'Total Pay'))

# open the file and iterate line by line
for line in file_name:
    line = line.strip()

    # if line is not blank
    if line != '':
        # split the line and capture each group
        (nm, wage, hours) = line.split()

        # name is in string, while wage and hours next
        # to be converted form stirng to float
        wage = float(wage)
        hours = int(hours)
        pay = wage * hours

        print('%-15s%-10d%-10.2f' % (nm, hours, pay))