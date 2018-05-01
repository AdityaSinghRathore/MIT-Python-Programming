#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 22:57:25 2017

@author: root
"""

x = 9
epi=0.01
nG=0
low=0.0
high=x
ans=(high + low)/2.0

while abs(ans**2 - x) >= epi:
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans = (high + low)/2.0
print(" numGuesses = " + str(nG))
print(str(ans)+" is close tosquare root of "+str(x))