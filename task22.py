#!/usr/bin/python
def calculate_coins(num):
	coins = [1,2,100,5,10,50,20]
	coins.sort()
	reverse = coins[::-1] """ za da izpozvame Greedy algorithm"""
	num *= 100
	coin = {}
	""" mega vernoto do tyka
	"""
	for i in reverse:
		modul = num // i
		print (modul)
		num = num - (num * modul)
	return coin
print (calculate_coins(0.54))