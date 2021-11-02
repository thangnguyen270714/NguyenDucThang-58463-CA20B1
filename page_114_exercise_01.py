"""
Author: Nguyen Duc Thang
Date: 24/09/2021
Program: page_114_exercise_01.py
Problem:Translate each of the following numbers to decimal numbers:
    a. 110012
    b. 1000002
    c. 111112
Solution:
    ....
"""
a='110012'
b='1000002'
c='111112'
sothapphana = 0
sothapphanb=0
sothapphanc=0
somua = len(a) - 1
somub = len(b) - 1
somuc = len(c) - 1
for soa in a:
    sothapphana= sothapphana + int(soa) * 2 ** somua
    somua = somua-1
print("110012=", sothapphana)
for sob in b:
    sothapphanb= sothapphanb + int(sob) * 2 ** somub
    somub = somub - 1
print("110012=", sothapphanb)
for soc in c:
    sothapphanc= sothapphanc + int(soc) * 2 ** somuc
    somuc = somuc -1
print("110012=", sothapphanc)