"""
Author: Nguyen Duc Thang
Date: 04/09/2021
Program: page_62_project_03.py
Problem: Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost.
Solution:
    ....
"""
# Initialize the constants
NEW_VIDEO=3.00
OLDIES_VIDEO=2.00
# Request the inputs
new=int(input('Hay nhap so luong dia moi can thue:'))
oldies=int(input('Hay nhap so luong dia cu can thue:'))
# Compute the results
tong=(NEW_VIDEO*new)+(OLDIES_VIDEO*oldies)
# Display the the results
print('Tong so tien:$'+str(round(tong,2)))


