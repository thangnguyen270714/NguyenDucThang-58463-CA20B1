"""
Author: Nguyen Duc Thang
Date: 26/09/2021
Program: page_132_project_05.py
Problem: A bit shift is a procedure whereby the bits in a bit string are moved to the left or
    to the right. For example, we can shift the bits in the string 1011 two places to
    the left to produce the string 1110. Note that the leftmost two bits are wrapped
    around to the right side of the string in this operation. Define two scripts,
    shiftLeft.py and shiftRight.py, that expect a bit string as an input. The script
    shiftLeft shifts the bits in its input one place to the left, wrapping the leftmost bit
    to the rightmost position. The script shiftRight performs the inverse operation.
    Each script prints the resulting string.
Solution:
    ....
"""
#Implementation of shiftRight method
#which performs inverse operation
def shiftRight(bitstring):
    bitstring=bitstring[len(bitstring)-1]+bitstring[0:len(bitstring)-1]
    return bitstring
#Get the input from user
bits = input("Enter a string of bits: ")
#call the shiftRight method which performs
#inverse operation
rightShift = shiftRight(bits)
#Display the output
print()
print(rightShift)
print()

