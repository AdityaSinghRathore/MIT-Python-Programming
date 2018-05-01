#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 02:06:27 2017

@author: root
"""

#%%
import random as r
a = r.randrange(1,101)
guess = int(input("take a guess: "))

while guess != a:
    if guess > a:
        print("Too High")
    elif guess < a:
        print("Too Low")
    guess = int(input("Guess Again:"))
print("You Are Right : ",guess," = ",a)
#%%
ans = int(input("Choose A No Between 0 and 100: "))

while True:
    if type(ans)!=int or ans>=100 or ans<0:
        print("Invalid Input only 0 to 99")
        ans = int(input("Choose A No Between 0 and 100: "))
    else:
        h = 99
        l = 0
        c = (h+l)//2
        while ans != c:
            if c < ans:
                print(c," is too low")
                l = c
            else:
                print(c," is too high")
                h = c
            c = (h+l)//2
        print("You are right", c, " = ", ans)
        break
#%%
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