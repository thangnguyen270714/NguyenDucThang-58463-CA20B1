"""
Author: Nguyen Duc Thang
Date: 12/09/2021
Program: page_85_exercise_01.py
Problem:Assume that x is 3 and y is 5. Write the values of the following expressions:
    a. x == y
    b. x > y – 3
    c. x <= y – 2
    d . x == y or x > 2
    e. x != 6 and y > 10
    f. x > 0 and x < 100
Solution:
    ....
"""

x=3
y=5
print('x=',x)
print('y=',y)
#a. x == y
if x==y:
    print('x==y,True')
else:
    print('x==y,False')
#b. x > y – 3
if x>y-3:
    print('x>y-3,True')
else:
    print('x>y-3,False')
#c. x <= y – 2
if x<=y-2:
    print('x<=y-2,True')
else:
    print('x<=y-2,False')
#d . x == y or x > 2
if x==y or x>2:
    print('x==y or x>2,True')
else:
    print('x==y or x>2,False')
#e. x != 6 and y > 10
if x!=6 and y>10:
    print('x!=6 and y>10,True')
else:
    print('x!=6 and y>10,False')
#f. x > 0 and x < 100
if x>0 and x<100:
    print('x>0 and x<100,True')
else:
    print('x>0 and x<100,False')




