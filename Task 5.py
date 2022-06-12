# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 07:14:13 2022

@author: nabin dahal

"""
"""
main menue ----------

1. add
2. Sub
3. Prd
4. Div
5. Rem
0. Exit
...............
Enter Your Choice : _1
................
Enter first no : _3
Enter second no : _5
Result : _8
...............

"""

#Declare

num1 = None
num2 = None
num3 = None
num4 = None
num5 = None
Num6 = None
Num7 = None
Num8 = None
Num9 = None

#input

num1 = input("Enter any number (1-6 ) : ")
num1 = int(num1)


if num1 == 1 : 
    print("Add ")
if num1 == 2 :
    print("Sub ")
if num1 == 3 :
    print("Prd ")
if num1 == 4 :
    print == ("Div ")
if num1 == 5 :
    print == ("Rem ")

    
# pocess
num7 = int(input("Enter First No : "))
num8 = int(input("Enter Second No : "))
if(num1 == 1) :
    num9 = num7 + num8   
elif(num1 == 2) :
    num9 = num7 - num8
elif(num1 == 3) :
    num9 = num7 * num8
elif(num1 == 4) :
    num9 = num7 / num8


#output
print("Result : ", num9)



