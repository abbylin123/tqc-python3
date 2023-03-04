# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:03:39 2022

@author: user
"""
l=[]
for i in range(4):
    print("Week %d:" %(i+1))
    for j in range(3):
        l.append(eval(input("Day %d:" %(j+1))))
print("Average: %.2f" %(sum(l)/12))
print("Highest:",max(l))
print("Lowest:",min(l))