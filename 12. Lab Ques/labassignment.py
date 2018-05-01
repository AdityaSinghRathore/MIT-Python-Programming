# -*- coding: utf-8 -*-
#%%
# Q1
def closest_power(base, num):
    '''
    base: base of the exponential , integer > 1
    num: number you want to be closest to, integer > 0    
    '''
    result = 0
    if base > 1 and num > 0:
        for i in range(num):
            if abs(base**i - num) <= abs((base**(i + 1)) - num):
                result = i
                break
    else:
        print("Base > 1, Num > 0")
    return result

print(closest_power(3, 12)) #gives 2
print(closest_power(4, 12)) #gives 2
print(closest_power(4, 1)) #gives 0
#%%
#Q2
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    if len(listA) == len(listB):
        sum = 0
        end = len(listA)
        for i in range(end):
            sum += listA[i]*listB[i]
        return sum
    else:
        print("Lists must be of the same length")
    
#%%
#Q3
O = {'a': 3, 'c': 2, 'b': 2, 'e': 3, 'd': 1, 'f': 2}
O.get('a',[])
O.items()
def dict_inverse(d):
    '''
    d: dict
    Returns
    '''
    ret = {}
    for k, v in d.items():
        ret[v] = ret.get(v, [])
        ret[v].append(k)
        ret[v].sort()
    return ret
        
print(dict_inverse(O))
#%%
#Q4
def sumDigits(N):
    if N==0:
        return 0
    else:
        return N%10 + sumDigits(N//10)
#%%
        
def dict_inversea(d):
    temp = {}
    for k ,v in d.items():
        if v in temp:
            temp[v].append(k)
            temp[v].sort()
        else:
            temp[v]=[k,]
    return temp
      
O = {'a': 3, 'c': 2, 'b': 2, 'e': 3, 'd': 1, 'f': 2}
print(dict_inversea(O))  