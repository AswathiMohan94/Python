# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:04:48 2020

@author: Aswathi Mohan
"""

def isprime(n):
    for i in range(2,n):
        if(n%i==0):
            return 1
      
n=int(input("enter the no : "))
n=isprime(n)
if(n==1):
    print("not prime so false")
else:
    print ("prime so true")
    