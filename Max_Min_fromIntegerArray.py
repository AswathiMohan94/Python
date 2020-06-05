# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:05:53 2020

@author: Aswathi Mohan
"""
class value :
    def max1(self,k):
        a=max(k)
        return a
    def min1(self,k):
        b=min(k)
        return b

k=[]
x=int(input("enter the limit : "))
for i in range(0,x,1):
    n=int(input())
    k.append(n)
c=value()
d=c.max1(k)
print("max value = ",d)
e=c.min1(k)
print("min value = ",e)

    