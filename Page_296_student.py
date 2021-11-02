"""
Author: Nguyen Duc Thang
Date: 1/11/2021
Program: page_296_student.py
Problem: Resources to manage a student's name and test scores

"""
from functools import reduce

class Student(object):
    """Represents a student."""
    def __init__(self, name, number):
        """Constructor creates a Student with the given
        name and number of scores and sets all scores to 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)

    def getname(self):
        """Returns the student's name."""
        return self._name

    def getscores(self):
        """Resets the ith score, counting from 1."""
        return self._scores

    def setscore(self,i,score):
        """Resets the ith score, counting from 1."""
        self._scores[i-1] = score

    def getscore(self,i):
        """Resets the ith score, counting from 1."""
        return self._scores[i-1]

    def getaverage(self):
        """Returns the average score."""
        sum = reduce(lambda x, y: x+y, self._scores)
        return sum/len(self._scores)

    def gethighscore(self):
        """Returns the highest score."""
        return max(self._scores)
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self._name + "\nScores: " + \
            " ".join(map(str, self._scores))

if __name__ == '__main__':
    print(help(Student))

    student_a = Student("Nguyen Duc Thang", 5)
    print("Name: ", student_a.getname())
    print("Score: ", student_a.getscores())
    print("Score in i: ", student_a.getscores(2))

    student_a.setscore(1, 9.0)
    print("Score in i: ", student_a.getscores(1))

    print("========" * 10)
    print(student_a)



