#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:12:59 2017

@author: root
"""

cube = 27
epi = 0.01
guess = 0.0
increment = 0.0001
ng = 0

while abs(guess**3 - cube) >= epi and guess <= cube:
    guess += increment
    ng += 1

print(' Num Guesses: ' + str(ng))
print(str(guess) + ' is close to the cuberoot of '+str(cube))