"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_109_exercise_01.py
Problem: 1. Write the encrypted text of each of the following words using a Caesar cipher with a distance value of 3:
    a. python
    b. hacker
    c. wow
Solution:
    ....
"""
#a. python
a='python'
b='hacker'
c='wow'
distance = 3
code = ""
code1 =""
code2 =""
for ch in a:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    code += chr(cipherValue)
print('python=:',code)
#b. hacker
for i in b:
    ordvalue1 = ord(i)
    cipherValue1 = ordvalue1 + distance
    code1 += chr(cipherValue1)
print('hacker=:',code1)
# c wow:
for n in c:
    ordvalue2 = ord(n)
    cipherValue2 = ordvalue2 + distance
    code2 += chr(cipherValue2)
print('wow=:',code2)
