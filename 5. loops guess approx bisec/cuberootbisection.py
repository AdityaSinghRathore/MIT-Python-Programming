#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:03:34 2017

@author: root
"""

cube = 56665
epi = 0.01
ng = 0
low = 0.0
high = cube
guess = (high + low)/2.0

while abs(guess**3 - cube) >= epi:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    ng += 1
print(" Num Guesses: " + str(ng))
print(str(guess) + " is close to cuberoot of " + str(cube))