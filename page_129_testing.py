"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_129_testing.py
Problem: Testing
Solution:
    Test driver for Flesch Index and Grade level

"""
sentences = int(input("Sentences: "))
words = int(input("Words: "))
syllables = int(input("Syllables: "))
index = 206.835-1.015 * (words / sentences)-\
84.6 * (syllables / words)
print("Flesch Index:", index)
level = round(0.39 * (words / sentences) + 11.8 * \
(syllables / words) -15.59)
print("Grade Level: ", level)