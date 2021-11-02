"""
Author: Nguyen Duc Thang
Date: 02/09/2021
Program: page_49_exercise_02.py
Problem: Explain the differences between the data types int and float.
Solution:
    Integers:
    As you learned in mathematics, the integers include 0, the positive whole numbers, and the
    negative whole numbers. Integer literals in a Python program are written without commas,
    and a leading negative sign indicates a negative value.
    Although the range of integers is infinite, a real computer’s memory places a limit on the
    magnitude of the largest positive and negative integers. The most common implementation of the int data type in many programming languages consists of the integers from
    2 2 2,147,483,648 ( 231) to 2,147,483,647 (231 2 1). However, the magnitude of a Python
    integer is much larger and is limited only by the memory of your computer. As an experiment, try evaluating the expression 2147483647 ** 100, which raises the largest positive
    int value to the 100th power. You will see a number that contains many lines of digits!

    Floating-Point Numbers:
    A real number in mathematics, such as the value of p (3.1416...), consists of a whole number, a decimal point, and a fractional part. Real numbers have infinite precision, which
    means that the digits in the fractional part can continue forever. Like the integers, real
    numbers also have an infinite range. However, because a computer’s memory is not infinitely large, a computer’s memory limits not only the range but also the precision that can
    be represented for real numbers. Python uses floating-point numbers to represent real
    numbers. Values of the most common implementation of Python’s float type range from
    approximately 210308 to 10308 and have 16 digits of precision.
    A floating-point number can be written using either ordinary decimal notation or
    scientific notation. Scientific notation is often useful for mentioning very large numbers.
    Table 2-4 shows some equivalent values in both notations.
    ....
"""