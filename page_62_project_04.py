"""
Author: Nguyen Duc Thang
Date: 04/09/2021
Program: page_62_project_04.py
Problem: Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume.
Solution:
    useful facts:
    diameter=2*radius
    circumference=diameter*3.14
    surface area=4*pi*radius*radius
    volume=4/3*pi*radius*radius*radius
    ....
"""
# Initialize the constants
radius=float(input('Enter the radius:'))
# Compute the results
diameter=2*radius
circumference=diameter*3.14
surface_area=4*3.14*radius*radius
volume=4/3*3.14*radius*radius*radius
# Display the the results
print('diameter=',diameter)
print('circumference=',circumference)
print('surface area=',surface_area)
print('volume='+str(round(volume,2)))


