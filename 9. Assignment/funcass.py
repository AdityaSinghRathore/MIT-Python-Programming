#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:36:44 2017

@author: root
"""
# 1
ans = int(input("Choose A No Between 0 and 100: "))
print("REMEMBER YOU CHOSE, ",ans)
while True:
    h = 99
    l = 0
    c = (h+l)//2
    while True:
        print("My guess ",c," Is it LOW(l) or HIGH(h) or EQUAL(e): ")
        x = input("(l/h/e) : ")
        if x=='l':
            print(c," is too low")
            l = c
        elif x=='h':
            print(c," is too high")
            h = c
        elif x=='e' or c==ans:
            print(c," it is")
            break
        else:
            print("Did not Understood your Input")
        c = (h+l)//2
    print("I am are right", c, " = ", ans)
    break
#%%
# 2

def square(a):
    return a**2
#%%
# 3

def evalQuadratic(a,b,c,x):
    return a*(x**2) + b*x + c

#%%
# 4
def fourthPower(a):
    return square(square(a))

#%%
# 5
def odd(a):
    return a%2!=0

#%%
# 6
def iterPower(base,exp):
    if type(exp)==int and exp>=0:
        ans = 1
        while exp > 0:
            ans *= base
            exp-=1
        return ans
#%%
# 7
def recurPower(base, exp):
    if exp>=0:
        if exp==0:
            return 1
        return base*recurPower(base, exp-1)
#%%
# 8
def gcd(a,b):
    for guess in range(min(a,b),0,-1):
        if a%guess == 0 and b%guess == 0:
            return guess

#%%
# 9
def euclidgcd(a,b):
    if b==0:
        return a
    return euclidgcd(b, a%b)
#%%
# 10
import math

def isIn(char, aStr):
    l = 0
    h = len(aStr)-1
    ans = (l+h)//2
    Flag = False
    steps = 0
    while Flag != True:
        print(aStr[ans])
        steps += 1
        if aStr[ans] == char:
            Flag = True
            break
        elif char > aStr[ans]:
            l = ans
        elif char < aStr[ans]:
            h = ans
        elif steps>math.log(len(aStr)):
            break
        ans = (l+h)//2
    return Flag

isIn("abcdefghijklm","b")