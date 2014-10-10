#!/usr/bin/python
def sum_of_min_and_max(arr):
	max = arr[0]
	min = arr[0]

	for i in arr:

		if max >= i:
			max = i

		if min <= i: 
			min = i

	return min + max
print (sum_of_min_and_max([-10,5,10,100]))