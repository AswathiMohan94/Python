# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:58:49 2020

@author: Aswathi Mohan
""" 
class printing:
    def prin(self):
        k=input("enter the string : ")
        print(k,"s" )
    
    def prin1(self):
        k=input("enter the string : ")
        print(k,"\n s" )

    def k(self,d):
        c=input("enter the string : ")
        print(c,d)
        
        
a=printing()
b=a.prin()
b=a.prin1()
d=input("integer argument to be passed : ")
e=a.k(d)