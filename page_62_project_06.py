"""
Author: Nguyen Duc Thang
Date: 04/09/2021
Program: page_62_project_06.py
Problem: The kinetic energy of a moving object is given by the formula KE 5 (1 2 / )mv2
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.
Solution:
    ....
"""
# Request the inputs
mass=float(input('Nhap khoi luong:'))
velocity=float(input('Nhap van toc:'))
# Compute the results
momentum=mass*velocity
kinetic_energy=(mass*velocity**2)/2
# Display the the results
print('Quan tinh =',momentum)
print('Dong Nang =',kinetic_energy)

