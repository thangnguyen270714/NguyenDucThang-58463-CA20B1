"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_109_exercise_03.py
Problem:You are given a string that was encoded by a Caesar cipher with an unknown distance value. The text can contain any of the printable ASCII characters. Suggest an
    algorithm for cracking this code
Solution:
    To decrypt this cipher text back to plaintext, you apply a method that uses
    the same distance value but looks to the left of each character for its replacement. This
    decryption method wraps around to the end of the sequence to find a replacement character for one near its beginning

    ....
"""