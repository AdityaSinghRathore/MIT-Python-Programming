x = int(input("Enter an Integer(perfect cube)"))
flag=0
guess=x//2
prev=guess
part=0

while flag==0:
	if guess**3==x:
		break
	elif guess**3>x:
		guess=(prev)//2
		prev=guess
		part=part+1
	else:
		guess=(prev+guess)//2
		prev=guess
		part=part+1

if guess**3==x:
	print(guess ," is the cube root of ",x," Partitions: ",part)
else:
	print(x ," is not a perfect cube.")