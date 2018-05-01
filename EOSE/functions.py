# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:06:42 2017

@author: Frndzzz
"""
#%%
def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print("Hi")
    return i%2 == 0
print(is_even(3))
print(is_even(8))

#%%
def func_a():
    print("inside func_a")
def func_b(x):
    print("inside func_b")
    return x
def func_c(z):
    print("inside func_c")
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))
#%%
def g(x):
    def h():
        x='abc'
        print(x)
    x=x+1
    print('in g(x): x = ',x)
    h()
    return x
x=3
z=g(x)
print(x)
#%%
def multi_iter(a,b):
    ans=0
    while b>0:
        ans+=a
        b-=1
    return ans
    
def multi_rec(a,b):
    if b==0:
        return a
    return a+multi_rec(a,b-1)

print(multi_rec(3,2))
print(multi_iter(3,2))
#%%
def isPalindrome(s):
    def toChar(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans                
    
    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])

    return isPal(toChar(s))
isPalindrome("1ada134")