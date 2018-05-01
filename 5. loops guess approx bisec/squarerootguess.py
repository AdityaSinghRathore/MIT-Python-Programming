#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:30:40 2017

@author: Aditya S Rarhore
"""
# programme to guess square roots

ans = 0
x = int(input("Enter A Number: "))
neg_flag=False

if x<0:
    neg_flag=True
    
while ans**2<x:
     ans+=1

if ans**2==x:
    print(ans," is the square root of ",x)
else:
    print(x," is not a perfect square ")
    if neg_flag:
        print("Did you mean ",-x)    

