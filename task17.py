#!/usr/bin/python
from __future__ import division
def slope_style_score(arr):
	biggest = arr[0]
	smallest = arr[0]
	total = 0
	for i in arr:
		if biggest < i:
			biggest = i
		if smallest > i:
			smallest = i
		total += i

	return (total - biggest - smallest) / (len(arr) - 2)

print (slope_style_score([96, 95.5, 93, 89, 92]))
print (slope_style_score([94, 95, 95, 95, 90]))