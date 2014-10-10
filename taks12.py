#!/usr/bin/python
def count_vowels(string):
	count = 0 
	vowels = ["a", "e", "i", "o", "u", "y"]

		for i in vowels:
			count += string.count(i)

	return count
print (count_vowels("Theistareykjarbunga"))	