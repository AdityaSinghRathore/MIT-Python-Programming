#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:42:59 2017

@author: root
"""

def func_a():
    print(" inside func_a ")

def func_b(x):
    print(" inside func_b ")
    return x

def func_c(y):
    print(" inside func_c ")
    return y() # if oyu dont put y() y will be treated as data

print(func_a())
print("\n*\n")
print(5 + func_b(2))
print("\n*\n")
print(func_c(func_a))