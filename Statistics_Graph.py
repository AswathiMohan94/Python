# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:03:50 2020

@author: Aswathi Mohan
"""
import matplotlib.pyplot as plt
import statistics
import numpy
class stdstats():

    def mean(self,n):
        m=[]
        print("the nos are : ")
        for i in range(0,n):
            a=int(input())
            i=i+1
            m.append(a)
        mean1=numpy.mean(m)
        print("mean = ",mean1)
        return m
            
    def median(self,n):
        p=[]
        print("the nos are : ")
        for j in range(0,n):
            c=int(input())
            j=j+1
            p.append(c)
        median1=numpy.median(p)
        print("mean = ",median1)
        
    def maxi(self,n):
        p=[]
        print("the nos are : ")
        for j in range(0,n):
            c=int(input())
            j=j+1
            p.append(c)
        r=max(p)
        print("max = ",r)
         
    def vari(self,n):
        p=[]
        print("the nos to find variance : ")
        for j in range(0,n):
            c=int(input())
            j=j+1
            p.append(c)
        r=statistics.variance(p)
        print("variance = ",r)
         
    def stddeviation(self,n):
        p=[]
        print("enter nos to find standard deviation : ")
        for j in range(0,n):
            c=int(input())
            j=j+1
            p.append(c)
        r=statistics.stdev(p)
        print("standard deviation  = ",r)
    
    def plotlines(self,g,f):
        self.x=g
        self.y=f
        plt.show()
        plt.plot(self.x,self.y)       
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.title("graph")
        
    def plotbars(self,g,f):
        self.x=g
        self.y=f
        y_position=numpy.arange(len(self.y))
        plt.show()
        plt.bar(y_position,align='center')
        plt.y(y_position)
        plt.xlabel("x axis")
        
        
    
    
        
    
    
b=stdstats()
n=int(input("enter the limit : " ))
print("enter", n," nos to find mean")
c=b.mean(n)
print("enter", n," nos to find median")
d=b.median(n)
d=b.maxi(n)
d=b.vari(n)
d=b.stddeviation(n)
g=[]
f=[]
print("the nos to plot graph")
print("x values are : ")
for j in range(0,n):
    c=int(input())
    j=j+1
    g.append(c)
print("y values are : ")
for k in range(0,n):
    d=int(input())
    k=k+1
    f.append(d)
d=b.plotlines(g,f)
d=b.plotbars(g,f)
   