# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 06:38:10 2022

@author: Nabin Dahal

"""
#Task 2
# a. create an array 4 obtained marks of students.

from array import array
#marks = 67,43,23,56

marks = array('i', [67,43,23,56])

print(marks)

print(marks[3])

# calculate total of obtained makrs

print(marks[0]+marks[1]+marks[2]+marks[3])
#calculated averae of total marks


print((marks[0]+marks[1]+marks[2]+marks[3])/4)

total = sum(marks)

print(total)

average = sum(marks)/4

print(average)

marks[2] =73

total = sum(marks)

print(total)

average = sum(marks)/4

print(average)

# find max marks

print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))
#calculate result of student (pm=40)?

class student :
    pass

#Use
s1 = student()
s2 = student()
print(type(s1))
print(type(s2))
