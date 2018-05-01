#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:37:15 2017

@author: root
"""

x = float(input(" Enter a positive integer between 0 and 1 "))

p = 0

while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0: # find the binary
    result = str(num%2) + result
    num = num//2

#shift right
for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print(' The binary representation of ' + str(x) + ' is '+result)