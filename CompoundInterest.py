# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:45:51 2020

@author: Aswathi Mohan
 """
class future:
    def f(self,c,r,t):
        a=c*((1+r)**t)
        return a

c=float(input("money invested = "))
r=float(input("coumpound interest rate per period = "))
t=float(input("year = "))
b=future()
f=b.f(c,r,t)
print("future value = ",f)