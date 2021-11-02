"""
Author: Nguyen Duc Thang
Date: 25/10/2021
Program: page_203_project_02.py
Problem: Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton.
    (Hint: The estimate of the square root should be passed as a second argument to the function.)
Solution:

"""
import math

# Initialize the tolerance
tolerance = 0.000001

def newton(x, estimate):
    """Returns the square root of x"""
    # Compute the difference and test for the base case
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        #Recurse after improving the estimate
        return newton(x, (estimate + x / estimate) / 2)

def main():
    """Allows the user to obtain square roots"""
    while True:
        #Receive the input number from the user
        x = input("Enter a positive number or enter/return to quit:")
        if x == "":
            break
        x = float(x)
        # Output the result
        print("The program's estimate is: ", newton(x, 1))
        print("Python's estimate is       ", math.sqrt(x))

main()