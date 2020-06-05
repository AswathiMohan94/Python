# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:18:14 2020

@author: Aswathi Mohan
"""
class collinear:
    def slope(self,x1,x2,x3,y1,y2,y3):
        ab=(y2-y1)/(x2-x1)
        bc=(y3-y2)/(x3-x2)
        ca=(y1-y3)/(x1-x3)
        if(ab==bc) and (bc==ca):
            return 1
        
        else:
            return 0
    def area(self,x1,x2,x3,y1,y2,y3):
        a=x1-x2
        b=x2-x3
        c=y1-y2
        d=y2-y3
        area=(1/2)*((a*d)-(b*c))
        if(area==0):
            return 1
        else:
            return 0
        
                
x1=float(input("X1 = "))
y1=float(input("y1 = "))
x2=float(input("X2 = "))
y2=float(input("y2 = "))
x3=float(input("X3 = "))
y3=float(input("y3 = "))
d=collinear()
e=d.slope(x1,x2,x3,y1,y2,y3)
f=d.area(x1,x2,x3,y1,y2,y3)
if(e==1)and (f==1):
    print("true so collinear")
else:
    print("false so not collinear")  