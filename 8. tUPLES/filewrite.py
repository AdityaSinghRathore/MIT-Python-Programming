#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 10:01:07 2017

@author: root
"""
#%%
nameHandle = open('names.txt','w')

for i in range(2):
    name = input("Enter name:" )
    nameHandle.write(name + '\n')
    
nameHandle.close()
#%%
# READING FILES

readHandle = open('names.txt','r')

for line in readHandle:
    print(line)

readHandle.close()

#%%