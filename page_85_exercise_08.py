"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_85_exercise_08.py
Problem: The variables x and y refer to numbers. Write a code segment that prompts the user for
an arithmetic operator and prints the value obtained by applying that operator to x and y.
Solution:
    ....
"""
x=float(input('Hay nhap x='))
y=float(input('Hay nhap y='))
print('Hay nhap so tuong ung voi phep tinh\n1=nhan\n2=chia\n3=cong\n4=tru')
toan=int(input('Hay nhap phep toan vs so tuong ung:'))
if toan==1:
    print('x*y=',x*y)
elif toan==2:
    print('x/y=',x/y)
elif toan==3:
    print('x+y=',x+y)
elif toan==4:
    print('x-y=',x-y)
else:
    print('False')