def cubicroot(n):
	start=flag=0
	end=n
	e = 0.00001

	while flag==0:
		mid = (start+end)/2
		error = abs(n-mid**3)

		if (error <= e):
			return mid

		if (mid**3>n):
			end=mid
		else:
			start=mid

x = int(input("Enter Any Number"))
print("Cube root of ",x, " is ",cubicroot(x))