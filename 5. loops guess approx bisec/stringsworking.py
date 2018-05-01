#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:44:14 2017

@author: Aditya S Rathore
"""
s="Marry had A Little Lamb"
print(len(s))
print(s[0])
print(s[1])
print(s[2])

b="abcdefgh"
# Used Like b[start : stop : step]
print(b[::-1])
print(b[3:6])
print(b[3:6])
print(b[-1])

# Strings are immuteable

s="hello"
s="y"+s[1:len(s)]
print(s)