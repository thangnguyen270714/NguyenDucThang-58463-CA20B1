"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_92_exercise_04.py
Problem:Describe the purpose of the break statement and the type of problem for which it is well suited.
Solution:
    The first thing to note is that the loop’s entry condition is the Boolean value True. Some
readers may become alarmed at this condition, which seems to imply that the loop will
never exit. However, this condition is extremely easy to write and guarantees that the body
of the loop will execute at least once. Within this body, the input datum is received. It is
then tested for the loop’s termination condition in a one-way selection statement. If the user
wants to quit, the input will equal the empty string, and the break statement will cause an
exit from the loop. Otherwise, control continues beyond the selection statement to the next
two statements that process the input
    ....
"""