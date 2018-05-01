#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:19:01 2017

@author: root
"""

x = 0.01
epi = 0.00001
ns = 0
low = x
high = 1
ans =  ( low + high )/2.0

while abs(ans**3 - x) >= epi:
    if ans**3 < x:
        high = ans
    else:
        low = ans
    ans =  ( low + high )/2.0
    ns += 1
print(ns, " Num Steps ")
print(str(ans) + " is close to cuberoot of "+ str(x))