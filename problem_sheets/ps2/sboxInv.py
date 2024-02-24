#!/usr/bin/env python

def sboxinv(state, roundkey): #Could be passed as anything but I wish for them to be Hex numbers as strings
	#pi_s = [4, 1, E, 8, D, 6, 2, B, F, C, 9, 7, 3, A, 5, 0]
	#This is what the example in lectures uses so we shall take it's inverse
	pi_s_inv = [F,1,6,C,0,E,5,B,3,A,D,7,9,4,2,8]
	#If we have input value, x, then we can get it's inverse by performing pi_s_inv[x] as the output would be the value that we had to feed to pi_s to get x
	#We don't need to account for +/-1 indexing because this is values 0-15 (0-F)
	#Python can already convert from number bases using int(value,base) and has a built in hex()
	#recall: substitution of an xor = the xor of the substitution of each
	invertedkey = ""
	for char in roundkey:
		invertedkey += pi_s_inv[int(char, 16)]

	#now to xor
	statue = state ^ invertedkey
	print(state)
