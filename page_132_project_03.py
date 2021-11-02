"""
Author: Nguyen Duc Thang
Date: 26/09/2021
Program: page_132_project_03.py
Problem: Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.
Solution:
    ....
"""
plainText=input('Ban muon ma hoa hay nhap A:\n Ban muon giai ma nhap B:\n')
text=input('Hay nhap van ban:')
distance = int(input("Enter the distance value: "))
code = ""
if plainText=='A':
    for ch in text:
        ordvalue = ord(ch)
        cipherValue = ordvalue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
    print(code)
elif plainText=='B':
    for ch in text:
        ordvalue = ord(ch)
        cipherValue = ordvalue - distance
        if cipherValue < ord('a'):
            cipherValue = ord('z') - (distance - (ord('a') - ordvalue - 1))
        code += chr(cipherValue)
    print(code)