#!/usr/bin/python
def prime_number_of_divisors(n):
	num_of_div = 0

	for i in range(1,n+1):

		if n % i == 0:

			num_of_div  = num_of_div + 1

	if (num_of_div % 2 == 0  and num_of_div != 2) or num_of_div == 1:
		return False
	else:
		return True

print prime_number_of_divisors(7)
print prime_number_of_divisors(8)
print prime_number_of_divisors(9)
