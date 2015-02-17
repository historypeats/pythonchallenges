#!/usr/bin/env python

# Challenge URL: http://www.pythonchallenge.com/pc/def/274877906944.html
# Solution: rot 2
# Next URL: http://www.pythonchallenge.com/pc/def/ocr.html

import sys
import string

CIPHERTEXT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
SPECIAL_CHARS = [' ', '.', '\'', '(', ')', '/', ':']

# Ciphertext decrypts to: i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

def usage():
	print 'usage: {0} [encrypt/decrypt] message rot_number'.format(sys.argv[0])


def decrypt(ciphertext, num):
	''' decrypt rotN '''

	# There are probably a few ways to solve this.
	# I'm just going to take the modulus of the alphabet and decrypt it that way. 

	# Make list of alphabet a..z
	alphabet = list(string.lowercase)
	
	plaintext = list()
	rotN = num
	
	for char in ciphertext:
		# Skip blanks
		if char in SPECIAL_CHARS :
			plaintext.append(char)
			continue

		# Get the index of the ciphertext char from the alphabet
		ct = alphabet.index(char)

		# Perform the modulus
		pt = (ct + rotN) % 26

		# Get plaintext char
		plaintext.append(alphabet[pt])

	return ''.join(plaintext)

def encrypt(plaintext, num):
	''' encrypt rotN '''

	alphabet = list(string.lowercase)
	ciphertext = list()
	rotN = num
	
	for char in plaintext:
		# Skip blanks
		if char in SPECIAL_CHARS :
			ciphertext.append(char)
			continue

		# Get the index of the ciphertext char from the alphabet
		ct = alphabet.index(char)

		# Perform the modulus
		pt = (ct - rotN) % 26

		# Get plaintext char
		ciphertext.append(alphabet[pt])

	return ''.join(ciphertext)


def main():
	''' main'''
	
	if len(sys.argv) < 4:
		usage()
		print '[!] Insufficient number of arguments.'
		sys.exit(-1)

	fnc = sys.argv[1]
	message = sys.argv[2]
	rotN = sys.argv[3]

	if 'encrypt' in fnc.lower():
		result = encrypt(message, int(rotN))
	elif 'decrypt' in fnc.lower():
		result = decrypt(message, int(rotN))
	else:
		usage()
		print '[!] Insufficient argument {0}'.format(func)
		sys.exit(-1)

	print 'Result: {0}'.format(result)

if __name__ == '__main__':
	main()