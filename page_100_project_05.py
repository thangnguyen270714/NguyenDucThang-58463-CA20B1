"""
Author: Nguyen Duc Thang
Date: 19/09/2021
Program: page_100_project_05.py
Problem:A local biologist needs a program to predict population growth. The inputs
would be the initial number of organisms, the rate of growth (a real number
greater than 0), the number of hours it takes to achieve this rate, and a number
of hours during which the population grows. For example, one might start with a
population of 500 organisms, a growth rate of 2, and a growth period to achieve
this rate of 6 hours. Assuming that none of the organisms die, this would imply
that this population would double in size every 6 hours. Thus, after allowing
6 hours for growth, we would have 1000 organisms, and after 12 hours, we would
have 2000 organisms. Write a program that takes these inputs and displays a prediction of the total population.
Solution:
    ....
"""
soluong=500
tocdo=2
thoigian=6
tangtruong=int(input('Hay nhap thoi gian tang truong:'))
tgtt=6/(500*2)
n=1
while n<=tangtruong:
    print('So thoi gian sau',n,'h Tang truong dc:',round(tgtt , 2))
    n+=1
    tgtt*=tangtruong





