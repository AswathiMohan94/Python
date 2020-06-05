# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:27:35 2020

@author: Aswathi Mohan
"""
import math
from fractions import Fraction
class week:
    def harmonic(self,a):
        self.no=a
        c=0
        for i in range(1,a+1):
            print(Fraction(1,i))
            s=c+Fraction(1,i)
            i=i+1
            c=s
        return(s)
        
    def sine(self,b):
        self.s=b
        c=math.sin(self.s)
        return(c)  
    def cosine(self,t): 
        self.c=t
        c=math.cos(self.c)
        return(c)
    
    def binary(self,d):
        self.d=d
        k=bin(self.d)
        return(k)
    
k=week()
a=int(input("enter the no : "))
a=k.harmonic(a)
print("the nth harmonic no is : ",a)
b=float(input("enter the angle :"))
b=k.sine(b)
print("sine value of the given angle is : ",b)
t=float(input("enter the angle :"))
t=k.cosine(t)
print("cosine value of the given angle is : ",t)
d=int(input("enter the integer : " ))
d=k.binary(d)
print("the binary equivalent is : ",d)