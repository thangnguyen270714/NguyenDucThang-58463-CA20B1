"""
Author: Nguyen Duc Thang
Date: 25/10/2021
Program: page_203_project_04.py
Problem: Restructure Newton’s method (Case Study 3.6) by decomposing it into three
    cooperating functions. The newton function can use either the recursive strategy
    of Project 1 or the iterative strategy of Case Study 3.6. The task of testing for the
    limit is assigned to a function named limitReached, whereas the task of computing a new approximation
    is assigned to a function named improveEstimate. Eachfunction expects the relevant
    arguments and returns an appropriate value
Solution:

"""
import math

# Initialize the tolerance
tolerance = 0.000001

def newton(x, estimate=1):
    """Returns the square root of x"""
    # Compute the difference and test for the base case
    if limitreached(x, estimate):
        return estimate
    else:
        # Recurse after improving the estimate
        return newton(x, improveestimate(x, estimate))

def limitreached(x, estimate):
    """Return true if the estimate is within the tolerance or false otherwise"""
    difference = abs(x - estimate ** 2)
    return difference <= tolerance

def improveestimate(x, estimate):
    """Return an improved estimate"""
    return (estimate + x / estimate) / 2

def main():
    """Allows the user to obtain square roots"""
    while True:
        x = input("Enter a positive number or enter/return to quit:")
        if x == "":
            break
        x = float(x)
        print("The program's estimate is: ", newton(x))
        print("Python's estimate is : ", math.sqrt(x))

main()