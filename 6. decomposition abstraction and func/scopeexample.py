#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:50:42 2017

@author: root
"""

#%%
def f(y):
    x=1
    x+=1

x=5
f(x)
print(x)

#%%
def g(y):
    print(x)
    print(x+1)

x=5
g(x)
print(x)
#%%
def h(y):
    x=x+1

x=5
h(x)
print(x)