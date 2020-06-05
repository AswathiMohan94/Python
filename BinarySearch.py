# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:25:51 2020

@author: Aswathi Mohan
"""


n=int(input("enter the no of elements to be included in the list : "))
list1=[]
for i in range(0,n,1):
    a=input()
    list1.append(a) 
print(list1)
c=input("enter the word to be searched : ")
for j in range(0,len(list1),1):
    if(list1[j]==c):
          d=list1.index(c)
print("\n\n the searched word is in the location",d)
    
