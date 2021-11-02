"""
Author: Nguyen Duc Thang
Date: 04/09/2021
Program: page_63_project_10.py
Problem: An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay.
Solution:
    ....
"""
# Request the inputs
wage=float(input('Enter the wage:$'))
regular_hours=float(input('Enter the regular hours:'))
overtime_hours=float(input('Enter the overtime hours:'))
# Compute the results
total_pay=(wage*regular_hours)+(wage*overtime_hours*1.5)
# Display the the results
print('The total weekly pay is:$'+str(round(total_pay,2)))


