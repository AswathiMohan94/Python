# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:53:13 2020

@author: Aswathi Mohan
"""
c=0
v=0
a=[]
n=int(input("enter the no : "))
a=input("enter the string : ")
for i in range(n):
    if(('a'<a[i]<'e')or('e'<a[i]<'i')or('i'<a[i]<'o')or('o'<a[i]<'u')or('u'<a[i]<='z')):
        c=c+1
    else:
        v=v+1
print("vowel = ",v)
print("consanents = ",c)

