"""
Author: Nguyen Duc Thang
Date: 1/11/2021
Program: Page_296_test_class_student.py
Problem: Resources to manage a student's name and test scores

"""
from Page_296_student import Student

if __name__ == '__main__':

    print(help(Student))

    student_a = Student("Nguyen Duc Thang", 5)
    print("Name: ", student_a.getname())
    print("Score: ", student_a.getscores())
    print("Score in i: ", student_a.getscores(2))

    student_a.setscore(1, 9.0)
    print("Score in i: ", student_a.getscores(1))

    print("========"*10)
    print(student_a)
