#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:26:46 2017

@author: root
"""

L1 = [1,2,3,4]
L2 = [1,2,5,6]
#%%
# The Index moves away
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
#%%
# The Index moves away
def remove_dupsl(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
#%%            
