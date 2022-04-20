# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:33:53 2021

@author: Latitude E5430
"""

a = int(input("Enter any integer : "))
b = 0
while a>0:
    digit = a%10
    b+=digit
    a = a//10
print(b)