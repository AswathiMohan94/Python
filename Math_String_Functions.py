# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 00:29:55 2020

@author: Aswathi Mohan
"""
import arith
import time
class tme:
    def sum(self,n):
        print("the sum of numbers from 0 to",n,"are")
        start=time.time()
        s=0
        for i in range(1,n+1):
            s=s+i
        end=time.time()
        print("start time : ",start)
        print("end time : ",end)
        
    
n=int(input("enter the limit : "))
b=tme()
a=b.sum(n)
c=arith.function()
  