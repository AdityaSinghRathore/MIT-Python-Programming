# -*- coding: utf-8 -*-

# Assignment PAGE 6 Solution
#%%
# Ques 1
test = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(x):
    temp = ()
    for i in range(0,len(x)+1,2):
        temp += (x[i],)
    return temp

oddTuples(test)

#%%
# Ques 2

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# A how_many
def how_many(x):
    """
     Input: Dictionary x
     Returns number of values associated with Dictionary x
    """
    s = 0
    for i in x:
        s += len(x[i])
    return s
print(how_many(animals))

#B Biggest
#using tuples

def biggest(x):
    t = ()
    for i in x:
        if len(t)==0:
            t = (i,len(x[i]))
        elif t[1]<len(x[i]):
            t = (i,len(x[i]))
    return t[0]

biggest(animals)    
#%%

def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    #clone = []
    #for i in list_of_numbers:
    #    clone.append(simple_divide(i,denom))
    # Using List Comprehension
    return [simple_divide(item,denom) for item in list_of_numbers]

def simple_divide(item, denom):
    try:
        return item/denom
    except ZeroDivisionError:
        return 0

fancy_divide([0,2,4,8,10],1)
#%%

    
#%%