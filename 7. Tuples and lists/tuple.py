# -*- coding: utf-8 -*-
#%%
te = () #empty tuple
t =  (2,"mit",3)
print(t[0])

a=(2,"mit",3) + (5,6)
print(a)
print(t[1:2])
print(t[1:3])
len(t)
#%%
#swapping values using tuples conveniently
x=1
y=2
print("**Before Swapping**")
print("X: ",x,", Y:",y)
(x,y) = (y,x)
print("**After Swapping**")
print("X: ",x,", Y:",y)

#%%
# Used to return more than one values from functions

def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return(q,r)

(quot, rem) = quotient_and_remainder(4,5)
#%%