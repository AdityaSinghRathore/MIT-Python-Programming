# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:32:40 2017

@author: Frndzzz
"""
#%%
# cuberoot guess and check
x=int(input("Enter an integer: "))
ans=0

while ans**3<x:
    ans=ans+1
if ans**3==x:
    print(str(ans) + " is the cuberoot of " + str(x))
else:
    print(str(x) + " is not a perfect cube")
#%%
#for negative sign
    
x=int(input("Enter an integer"))
ans = 0

while ans**3 < abs(x):
    ans += 1
    
if ans**3>abs(x):
    print(str(x) + " is not a perfect cube")
else:
    if x<0:
        ans=-ans
    print(str(ans) + " is the cuberoot of " + str(x))
#%%
# Guess and check cuberoot

cube = 8

for i in range(cube+1):
    if i**3>=abs(cube):
        break

if i**3!=abs(cube):
    print(str(cube) + " is not a perfect cube")
else:
    if cube<0:
        i=-i
    print(str(i) + " is the cuberoot of "+str(cube))
#%%
for i in range(5):
    print(i)
#%%