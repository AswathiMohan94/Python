# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:42:46 2020

@author: Aswathi Mohan
"""
import sys
print(sys.argv)
class fact:
    def factorial(self,  n):
        f=1
        for i in range(1,n+1):
            f=f*i
        return(f)
       
n=sys.argv[1] 
n=int(n)
k=fact()
a=k.factorial(n)
print("factorial : ",a)