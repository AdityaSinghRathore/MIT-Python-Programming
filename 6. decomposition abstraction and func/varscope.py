#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:29:50 2017

@author: root
"""

def g(x):
    def h():
        x = 'abc'
    x = x+1
    print(" in g(x) x is ",x)
    h()
    return x

x=3
z=g(x)

print(x)
print(z)