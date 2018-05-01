x = int(input("Enter a number"))

for guess in range(abs(x)+1):
	if guess**3>=x:
		break

if guess**3==x:
	print(guess ," is the cube root of ",x)
else:
	print(x ," is not a perfect cube.")