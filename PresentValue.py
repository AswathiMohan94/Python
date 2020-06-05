# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:26:02 2020

@author: Aswathi Mohan
"""

class present:
    def p(self,c,r,t):
        a=c/((1+r)**t)
        return a

c=float(input("c = "))
r=float(input("rate = "))
t=float(input("period = "))
b=present()
p=b.p(c,r,t)
print("present value = ",p)