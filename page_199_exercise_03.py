"""
Author: Nguyen Duc Thang
Date: 24/10/2021
Program: page_199_exercise_03.py
Problem:Write the code for a reducing that creates a single string from a list of strings named words.
Solution:

"""
words = ['hello','world']
from functools import reduce
print(reduce(lambda x,y:x+y,map(lambda x:x[0],words)))