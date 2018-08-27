def sumofdigit(n):
	s=input("Enter the no")
	while n:
		s+=n%10
		n//=10
	print(n,'is the factorial')
