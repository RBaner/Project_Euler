def prime_recursion(num):
  divisor = False
	for i in range(2,int(num/2)):
		if num%i == 0:
			divisor = i
			break
	if type(divisor) == int:
		output = [divisor] + prime_recursion(num/divisor)
	else:
		output = [num]
	return(output)
