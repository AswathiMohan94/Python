# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:25:30 2020

@author: Aswathi Mohan
"""

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
        