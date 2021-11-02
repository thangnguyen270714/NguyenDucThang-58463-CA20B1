"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_114_exercise_02.py
Problem: Translate each of the following numbers to binary numbers:
    a. 4710
    b. 12710
    c. 6410
Solution:
    ....
"""
#a.4710
a=4710
b=12710
c=6410
sonhiphana = ""
sonhiphanb = ""
sonhiphanc = ""
while a>0 :
    phandua = a % 2
    phanduc = c % 2
    phandub = b % 2
    a = a // 2
    b = b // 2
    c = c // 2
    sonhiphana = str(phandua) + sonhiphana
    sonhiphanb = str(phandub) + sonhiphanb
    sonhiphanc = str(phanduc) + sonhiphanc
print("So nhi phan 4710 là:",sonhiphana,'\nSo nhi phan 12710 là:',sonhiphanb,'\nSo nhi phan 6410 là:',sonhiphanc)