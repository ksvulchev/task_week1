#!/usr/bin/python
def sevens_in_a_row(arr, n):
	count = 0
	for i in arr:
		if i == 7:
			count = count + 1
			if count == n:
				return True
		else:
			count = 0
	return False

print (sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
print (sevens_in_a_row([1,7,1,7,7], 4)
print (sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
print (sevens_in_a_row([7,2,1,6,2], 1))
