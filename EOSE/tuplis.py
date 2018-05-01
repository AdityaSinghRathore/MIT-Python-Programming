# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:27:14 2017

@author: Frndzzz
"""

#%%
te = ()
t = (2,"one", 3)

t[0]
(2,"one",3) + (5,6)
t[1:2]
t[1:3]
t[1] = 4

#%%
def quotient_and_remainder(x, y):
    q = x//y
    r = x%y
    return (q,r)

(quot, rem) = quotient_and_remainder(4,5)
print(quot,rem)
#%%
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

print(get_data(((1,'a'),(2,'b'),(3,'a'))))
#%%
#LISTS
a_list = []
b_list = [2, 'a', 4, True]
L = [ 2, 1, 3]
L[0]
L[2]+1
# L[3] gives error
L[1] = 5
L

# Sum of elements in a list

total = 0
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L:
    total += i
print(total)
#%%
# operations on lists
L = [2,1,3]
L.append(5) 

L1 = [2,1,3]
L2 = [4,5,6]

L3 = L1 + L2
print(L3)
L1.extend([0,6])
print(L1)
#%%
L = [2,1,3,6,3,7,0]
L.remove(2)
print(L)
L.remove(3)
print(L)
del(L[1])
print(L)
L.pop()
print(L)

#%%
# Lists to strings and back
s = "I <3 Big Data"
list(s)
s.split('<')
L = ['a', 'b', 'c']
''.join(L)
'_'.join(L)
#%%
L = [9,6,0,3]
sorted(L) #does not mutate
L.sort() #does mutate
L
L.reverse()
L
#%%
# SPECIAL procedure range
# returns something that behaves like a tuple
for i in range(5,2,-1):
    print(i)
#%%
# append and aliases
    
warm = ['red', 'yellow', 'orange']
hot = warm

hot.append('pink')
print(warm)
print(hot)
#%%
# Cloning a list creates a new list

cool = ['blue', 'green', 'grey']
chill = cool[:]

chill.append('black')
print(chill)
print(cool) 

#%%

warm = ['red','yellow','orange']
sw = warm.sort()
print(warm)
print(sw)

cool = ['blue', 'green', 'grey']
sc = sorted(cool)
print(cool)
print(sc)
#%%
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]

brightcolors.append(hot)
print(brightcolors)

hot.append('pink')
print(hot)
print(brightcolors)

print(hot + warm)
print(hot)
#%%
def rem_dups(L1,L2):
    L1_c = L[:]
    for e in L1_c:
        if e in L2:
            L1.remove(e)
    
L1 = [1,2]
L2 = [2,3]    
rem_dups(L1,L2)
print(L1)