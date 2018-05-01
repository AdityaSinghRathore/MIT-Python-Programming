#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:47:18 2017

@author: aditya-HP
"""

#%%
# PRIME NUMBER GENERATOR 

def genprimes():
    d={}
    q=2
    while True:
        if q not in d:
            yield q
            d[q*q]=[q]
        else:
            for p in d[q]:
                d.setdefault(p+q,[]).append(p)
            del d[q]
        q+=1

#%%
# QUESTION 2
class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.getX()) + "," + str(self.getY()) + ">"
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def __eq__(self,other):
        return self.getX() == other.getX() and self.getY() == other.getY()
        
    def __repr__(self):
        return "Coordinate("+str(self.getX())+","+str(self.getY())+")"
c = Coordinate(3,4)
o = Coordinate(3,4)

print(c==o)
print(eval(repr(c)) == c)
print(isinstance(c,Coordinate))
#%%
# QUESTION 3

# Integer Set Class

class intSet(object):
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        if e not in self.vals:
            self.vals.append(e)
            
    def member(self,e):
        return e in self.vals
    
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " Not found")
            
    def __str__(self):
        self.vals.sort()
        result = ''
        #for e in self.vals:
        #   result = result + str(e) + ','
        #return '('+result[:-1]+')'
        return '{'+ ','.join([str(e) for in self.vals]) +'}'
    
    def intersect(self, other):
       
        commonVals = intset()

        for x in self.vals:
            if other.member(x):
                commonVals.insert(x)
        return commonVals

    def __len__(self):
        return len(self.vals)

s = intSet()
s.insert(3)
s.insert(4)
s.insert(3)
print(s)

s.member(3)
s.member(6)

s.remove(3)
s.insert(6)

print(s)

s.remove(3)