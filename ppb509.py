# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:28:57 2022

@author: user
"""
import math

def compute(p,q):
    return math.gcd(p,q)

x,y=eval(input())
m,n=eval(input())
p=(x*n+y*m)/compute(x*n+y*m,y*n)
q=(y*n)/compute(x*n+y*m,y*n)

print("%d/%d + %d/%d = %d/%d" %(x,y,m,n,p,q))