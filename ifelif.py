# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 06:17:17 2022

@author: nabin dahal
"""

# if elif statement (if... elself)

"""
    if condition1:
        statement (s)
    elif condition2:
        statement (s)
    ..........
elif conditionN:
    statement(s)
else:
    statements(s)
"""
"""
# write a program shich accept number (day value)
# print weekday.
#Declare
num1 = None
result = None

# Input
num1= input("Enter any number (1-7) : ")


# Process
num1 = int(num1)
if num1 == 1:
    result = "sun"
elif num1 == 2 :
    result = "mon"
elif num1 == 3 :
    result == "tue"
elif num1 == 4:
    result == "wed"
else:
    result = "other"
    
    
# Output
print("result : ", result)

"""
# Neste inf statement
"""

if condition1 :
    if condition2:
        statement (s)
"""
"""
# find largest number among 3 numbers.

#Declare
num1 = None
num2 = None
num3 = None
num4 = None

#Inpurt
num1 = input("Enter any number : ")
num2 = input("Enter any number : ")
num3 = input("Enter any number : ")

#process
num1 = int(num1)
num2 = int(num2)
num2 = int(num3)
if(num1>=num2):
    if(num1>=num3):
        num4 = num1
if(num2>=num1):
    if(num2>=num2):
        num4 = num2

if(num3>=num1):
    if(num3>=num2):
        num4= num3
#output

print("Largest number : ", num4)
"""

# write a program which print largest number
# among three numbers.

# systax

"""
if condition and/or conditon2 and and /or consntion3 :
        statement(s)
"""

#example
#declare
num1 = None
num2 = None
num3 = None
num4 = None

# input

num1 = input("Enter Fist no : ")
num2 = input("Enter Second no : ")
num3 = input("Enter Third no : ")

# pocess

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1>=num2 and num1>=num3:
    num4=num1
elif num2>=num1 and num2>=num3:
    num4=num2
elif num3>=num1 and num>=num2:
    num4=num3

#output
print("Result : ", num4)