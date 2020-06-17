# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:46:10 2020

@author: TEJASHRI
"""
import matplotlib.pyplot as plt 
 
y=[]
x=[]
a=1
while(a==1):
    i=0
    n=int(input("enter a no="))
    x.append(n)
    while(n!=1):
        if(n%2==0):
            n=n/2
            print(n)
        else:
            n=(3*n)+1
            print(n)
        i=i+1
        
    y.append(i)
    
    print("Number of itteration for given ip=")
    print(i)
    a=int(input("do you want to continue? If yes enter 1, else enter 0="))
    
    
 #plot for number of iterations needed for a given input  
plt.plot(x,y)
# naming the x axis 
plt.xlabel('input value') 
# naming the y axis 
plt.ylabel('number of itterations') 
plt.title('number of iterations needed for a given input') 
plt.show() 


#Histogram
# setting the ranges and no. of intervals 
range = (0,100)
bins = 10 
  
# plotting a histogram 
#plt.hist(x, bins, range, color = 'blue', histtype = 'bar', rwidth = 0.8) 

plt.hist(x,bins,range) 
# x-axis label 
plt.xlabel('Input Number') 
# frequency label 
plt.ylabel('No. of itterations')  
plt.title('histogram of Number and itterations') 
plt.show() 
   
    