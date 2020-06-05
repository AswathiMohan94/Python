# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:50:03 2020

@author: Aswathi Mohan
"""

class stdin():
    def empty(self):
        a=input("enter string or emptyspace : ")
        b=a.isspace()
        if(b==True):
            print("space or empty")
        else:
            print(a)
        
    def readint(self,b):
        self.b=b
        c=ord(self.b)
        print(c)
        
    def boolean(self,d):
       self.b=b
       if((0<=self.b>=9) or ('a'<=self.b>='z') or('A'<=self.b>='Z')):    
           return(1)
       else:
                return(0)
        
        
             
                


c=stdin()
d=c.empty()
b=input("enter a character : ")
f=c.readint(b)
d=input("enter identifier : ")
d=c.boolean(d)
if(d==1):
    print("True")
else:
    print("False")