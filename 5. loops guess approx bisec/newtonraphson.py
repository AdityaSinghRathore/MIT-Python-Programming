#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:27:18 2017

@author: root
"""

epi = 0.01
y = 121.0
guess = y/2.0
ng = 0

while abs(guess**2-y) >= epi:
    ng += 1
    guess = guess - (guess**2 - y)/(2*guess)
print(" Num Guesses: " + str(ng))
print(str(guess)+" is close to squareroot of "+str(y))