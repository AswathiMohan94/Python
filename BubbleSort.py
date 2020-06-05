# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:29:36 2020

@author: Aswathi Mohan
"""
list1=[]
n=int(input("enter the no of elementsto be included in the list : "))
for m in range(0,n,1):
    b=input()
    list1.append(b)
    
print(list1)
print("\n")
print("the sorted list in ascending order is\n")
for i in range(0,(len(list1)-1)):
    for j in range(0,(len(list1)-1)):
        if(list1[j]>list1[j+1]):
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
            
    
    
