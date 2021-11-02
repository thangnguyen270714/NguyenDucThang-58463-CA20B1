"""
Author: Nguyen Duc Thang
Date: 04/09/2021
Program: page_63_project_09.py
Problem: Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.
    Use the following approximations:
    • A kilometer represents 1/10,000 of the distance between the North Pole and
    the equator.
    • There are 90 degrees, containing 60 minutes of arc each, between the North
    Pole and the equator.
    • A nautical mile is 1 minute of an arc.
Solution:
    useful facts:
    1 kilometer= 1/10,000 of the distance between the North Pole and the equator.
    There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
    1 degree = 60 minutes of arc
    1 nautical mile = 1 minute of an arc
    ....
"""
# Request the inputs
klicks=float(input('Enter the number of kilometer:'))
# Compute the results
nauts=klicks*90*60/10000.0
# Display the the results
print('The number of nautical miles:',nauts)
