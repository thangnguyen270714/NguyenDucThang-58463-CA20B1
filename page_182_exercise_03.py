"""
Author: Nguyen Duc Thang
Date: 24/10/2021
Program: page_182_exercise_03.py
Problem: Describe the costs and benefits of defining and using a recursive function.
Solution:
    - Benefits:
    + Recursive solutions are often more natural and elegant than their iterative
    counterparts
    + Recursive function arises when the programmer fails to specify the base case or to reduce
    the size of the problem in a way that terminates the recursive process
    - The costs:
    + The run-time system on a real computer, such as the PVM, must devote some overhead to recursive function calls
    + When, because of a design error, the recursion is infinite, the stack
    frames are added until the PVM runs out of memory, which halts the program with an
    error message.
    + By contrast, the same problem can often be solved using a loop with a constant amount of
    memory, in the form of two or three variables. Because the amount of memory needed for
    the loop does not grow with the size of the problem’s data set, the amount of processing
    time for managing this memory does not grow, either.
    + some problems with an iterative solution must still use an
    explicit stack-like data structure, so a recursive solution might be simpler and no less
    efficient.


"""