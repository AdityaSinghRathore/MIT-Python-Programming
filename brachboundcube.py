x = int(input("Enter a er"))
flag=0
guess=x//2

while flag==0:
	if guess**3==x:
		break
	elif guess**3>x:
		guess=(guess+x)/2
	else:


if guess**3==x:
	print(guess ," is the cube root of ",x)
else:
	print(x ," is not a perfect cube.")