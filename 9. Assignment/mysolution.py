# -*- coding: utf-8 -*-

#%%
# 1

print('Hello World!')
#%%
# 2
happy = int(input("Enter An Integer :"))

if happy>2:
    print("hello world")
#%%
# 3
varA = 1
varB = 2

if type(varA) == str or type(varB) == str:
    print("String involved")
elif type(varA) == int and type(varB) == int:
    if varA>varB:
        print("bigger")
    elif varA<varB:
        print("smaller")
    else:
        print("equal")
    
#%%
# 4
i = 0
while i<10:
    i += 2
    print("prints",i)
    
#%%
# 5
print("prints Hello!")
i = 10
while i>0:
    print("prints",i)
    i -= 2
#%%
# 6
print("** SUM N NUMBERS **")
x = int(input("Enter a No. :"))
i = 0
sum = 0
while i<=x:
    sum += i
    i += 1

print(sum)

#%%
# 7
for i in range(2,12,2):
    print(i)
#%%
# 8
print("Hello!")

for i in range(10,0,-2):
    print(i)    
#%%
# 9
print("** SUM N NUMBERS **")
x = int(input("Enter a No. :"))
sum = 0
for j in range(x+1):
    sum += j
print(sum)
#%%

iteration = 0
count = 0
s = "hello, world"


for iteration in range(5):
    i = 0
    while i < len(s):
        count += 1
        i += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
#%%
# 11 A
s = 'azcbobobegghakl'
a = 'aeiou'
numVows = 0

for i in range(len(s)):
    if s[i] in a:
        numVows += 1
print(" Number of vowels : ",numVows)

#%%
# 11 B
t = 'azcbobobegghakl'
p = 'bob'
n = len(t)
m = len(p)
count = 0

for i in range(n-m):
    if p == s[i:i+m]:
        count += 1
print(p + " Occurs " + str(count) + " times in " + t)
#%%
# 11 C

s = 'azcbobobegghakl'
r = ''
c = ''

for char in s:
    if c=='':
        c=char
    elif c[-1] <= char:
        c += char
    elif c[-1] > char:
        if len(r) < len(c):
            r = c
            c = char
        else:
            c = char
if len(c) > len(r):
    r=c
print(r)