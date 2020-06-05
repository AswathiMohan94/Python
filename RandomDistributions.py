# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:42:06 2020

@author: Aswathi Mohan
"""
import statistics
import random
import matplotlib.pyplot as plt
import cmath
import numpy
class rand():
    def u(self,n):
        print(n,"float nos between 1 & 3 = ")
        for i in range(0,n):
            i=random.uniform(0,2)
            i=i+1
            print(i)
    def seed(self,n):
        print("random no with seed")
        for i in range(n):
            random.seed(0)    
            print(random.randint(1,10))
            
    def shuffle_nos(self,n):
        p=[]
        print("enter",n,"nos = ")
        for i in range(0,n):
            a=input(list())
            i=i+1
            p.append(a)
        print(p)
        
        random.shuffle(p)
        print(p)
            
   
    def ber(self,n):
        p=[]
        print(n,"trials and nos are = ")
        for i in range(0,n):
            a=int(input())
            i=i+1
            p.append(a)
        s=numpy.random.binomial(p,0.5,n)
        print(s)
        plt.hist(s,density=True,color="yellow")
        
    def guassian(self,n):
        m=[]
        p=[]
        print("the nos are : ")
        for i in range(0,n):
            a=int(input())
            i=i+1
            m.append(a)
            x=cmath.sqrt(2*3.14)
            b=1/x
            c=(i)
        mean1=numpy.mean(m)
        print("mean = ",mean1)
        r=statistics.stdev(p)
        print("standard deviation  = ",r)
       
    
          
b=rand()
n=int(input("enter the limit : " ))
c=b.u(n)
c=b.seed(n)
c=b.shuffle_nos(n)
c=b.ber(n)