"""
Author: Nguyen Duc Thang
Date: 26/09/2021
Program: page_133_project_06.py
Problem:Use the strategy of the decimal to binary conversion and the bit shift left operation defined in Project 5
to code a new encryption algorithm. The algorithm should add 1 to each character’s numeric ASCII value, convert it to a bit string,
and shift the bits of this string one place to the left. A single-space character in the encrypted string separates the resulting bit strings
Solution:
    ....
"""
def shiftRight(bitstring):
    bitstring=bitstring[len(bitstring)-1]+bitstring[0:len(bitstring)-1]
    return bitstring
a=int(input('Nhap so:'))
sonhiphana = ""
while a>0 :
    phandua = a % 2
    a = a // 2
    sonhiphana = str(phandua) + sonhiphana
rightShift = shiftRight(sonhiphana)
print()
print('So nhi phan',rightShift)