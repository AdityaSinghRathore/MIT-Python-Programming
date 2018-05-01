#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 22:50:50 2017

@author: root
"""

s="abcdefgh"

for i in range(len(s)):
    if s[i] == 'i' or s[i] == 'u':
        print("There is an i or u")
        
for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")