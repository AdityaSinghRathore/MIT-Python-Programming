#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 23:52:19 2017

@author: root
"""
#%%
te = ()
t = (2,"one",3)
t[0]
(2,"one",3) + ("Maa","Kaa")

t[1]
t[1:2]
t[1:3]
t[1] = 4
#%%
x=1
y=3

print(x,y)

x = x + y
y = x - y
x = x - y

print(x,y)
#%%
x=1
y=3
print(x,y)
(x,y) = (y,x)
print(x,y)