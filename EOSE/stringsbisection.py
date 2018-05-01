# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:41:05 2017

@author: Frndzzz
"""

#%%
s = "abcdefgh"
# <>[start:stop:step]
print(s[::-1])
print(s[3:6])
print(s[-1])
#%%
#stings and loops
s = "abcdefgh"
c = ''

for c in s:
    if c=='e' or c=='u':
        print("There is an e or u")
print(type(s))
print(type(c))
#%%
# Approximate Solution

cube=27
epsilon=0.01
guess=0.0
increment=0.0001
num_guesses=0

while abs(guess**3 - cube) > epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("No. of guesses ",num_guesses)    
if abs(guess**3-cube) >= epsilon:
    print("Failed on cuberoot of ",cube)
else:
    print(guess, " is close to cuberoot of ",cube)
    
#%%
# Bisection Search
# cuberoot bisection
    
x=27
epsilon=0.01
ng = 0
low = 0
high = x
ans = (low+high)/2.0

while abs(ans**3 - x) > epsilon:
    #print("Low: "+str(low)+" High: "+str(high)+" Ans: "+str(ans))
    ng+=1
    if ans**3<x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print(" NumGuesses: "+ str(ng))
print(str(ans) + " is close to squareroot of "+str(x))
#%%
epsilon = 0.01
y=27.0
guess=y/2.0
ng = 0

while abs(guess**3-y)>epsilon:
    guess = guess - (guess**3 - y)/(3*guess**2)
    ng+=1
print("Num Guesses: ",ng)
print(guess," is close to cube root of ", y)    