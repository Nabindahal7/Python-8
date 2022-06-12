# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 06:09:09 2022

@author: USER
"""

# Array

from array import array #step 1
#declare an array

weights = array('i', [6,7,8,9,10])
# index            0,1,2,3,4

#print(help(array))
print(weights) #all elements

weights[0]=62
print(weights)
print(weights[3])