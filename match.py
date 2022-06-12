# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 06:15:21 2022

@author: USER
"""

# import library

import sys



# sys.exit()
# quit()

#Alternate of elif statement

#match case statement
# declare

num1 = None
result = None

# input

num1 = input("Enter number (1 -7 ) : ")
match num1 :
    case 1 :
        print ("One")
    case 2 :
        print ("Two")
    case 3 :
        print ("Three")
    case 4 :
        print ("Four")
    case 5 :
        print ("Five")
    case 6 :
        print ("Six")
    case 7 :
        print ("Seven")
    case_default :
        print ("Other")
        
# process
num1 = int(num1)

# output
print("Result : ", result)
