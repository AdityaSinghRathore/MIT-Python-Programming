# -*- coding: utf-8 -*-

print("**FINDING SQUARE ROOTS**")
x = int(input("Enter a no. :"))

g = x/2
epi = 0.01

while g*g - x > epi:
    g  = g + (g + g/x)/2

print(g," is close to square root of ",x)
