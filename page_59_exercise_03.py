"""
Author: Nguyen Duc Thang
Date: 02/09/2021
Program: page_59_exercise_03.py
Problem: Explain how to display a directory of all of the functions in a given module
Solution:
    Functions and other resources are coded in components called modules. Functions like
abs and round from the __builtin__ module are always available for use, whereas the
programmer must explicitly import other functions from the modules where they are
defined.
The math module includes several functions that perform basic mathematical operations.
The next code session imports the math module and lists a directory of its resources:
>> import math
>> dir(math)
['__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'acos', 'acosh', 'asin',
'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp',
'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose',
'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log',
'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow',
'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau',
'trunc']
    ....
"""