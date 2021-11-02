"""
Author: Nguyen Duc Thang
Date: 26/09/2021
Program: page_133_project_07.py
Problem:Write a script that decrypts a message coded by the method used in Project 6
Solution:
    ....
"""
def shiftLeft(bitstring):
    bitstring = bitstring[1:]+bitstring[0]
    return bitstring
a=str(input('Nhap so nhi phan:'))
leftShift = shiftLeft(a)
sothapphana = 0
somua = len(a) - 1
for soa in a:
    sothapphana= sothapphana + int(soa) * 2 ** somua
    somua = somua-1
print('So thap phan la:',sothapphana)
