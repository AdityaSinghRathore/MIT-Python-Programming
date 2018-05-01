# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
print("Hello")
i = 0
j = 1
while True:
    i*=j
    j*=i
    print(j)
#%%\
x=input("Enter an integer")
x=int(x)

if(x%2==0):
    print(str(x), " is even")
else:
    print(str(x), " is odd")

print("Done with conditional")
#%%
print("Comparison among three numbers")
x=input("Enter first number")
y=input("Enter second number")
z=input("Enter third number")

if x<y and x<z:
    print(str(x)," is least")
elif y<z:
    print(str(y)," is least")
else:
    print(str(z)," is least")
    
#%%
'ab' + 'cd'
3*'atul'
len('atul')
'atul'[1]
'atul'[1:3]
#%%
text = input("Type anything...")
print(5*text)

num = int(input("Type a number..."))
print(5*num)
#%%