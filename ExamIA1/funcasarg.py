#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 01:11:12 2017

@author: root
"""

#%%
def fact(x):
    if x == 1:
        return 1
    return x*fact(x-1)

def applyToEach(L,f):
    """
    Applies f() to every element in L 
    """
    for i in range(L[i]):
        L[i] = f(L[i])
        
L = [1,2,3,4,5]
print(applyToEach(L,fact))
#%%