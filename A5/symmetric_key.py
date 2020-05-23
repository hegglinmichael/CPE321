from Crypto.Cipher import AES
import sys
import os

# array to hold cipher text
cipher_text = []

def encrypt(text, key):
	return key.encrypt(text)

# read data into file in byte sized chunks
def readfile(filename):
	# array to hold plain text blocks
	pt = []
	# holds all text
	total = ""
	# holds blocks of data
	temp = ""
	head = ""

	# open file for reading
	with open(filename, "r") as fd:
		lines = fd.readlines()
		fd.close()

	# add lines together
	for line in lines:
		total += str(line)

	head = total[0:39]
	cipher_text.append(head)
	total = total[39:]
		
	# put into multiple of 16 bytes
	while (len(total) % 16 != 0):
		total += "i"

	for i in range(len(total) + 1):
		if i % 16 == 0 and temp != "":
			pt.append(temp)
			temp = ""

		if i == len(total):
			break

		temp += total[i]

	return pt


# Description
#	writes data to output file
def write_encrypted_data(cipher_text, fd):
	for block in cipher_text:
		fd.write(str(block))

# Description:
#  method xors two strings of the same length together
#  if strings aren't the same length an error is thrown
#
def XOR(str1, str2):
	mod_str = ""

	if len(str1) != len(str2):
		print("strings are of different length: exiting")
		print(len(str1))
		print(len(str2))
		return

	for i in range(len(str1)):
		temp_xor = ord(str1[i]) ^ ord(str2[i])
		hex_temp = hex(temp_xor)[2:]
		hex_str = str(hex_temp)

		if len(hex_str) == 1:
			hex_str = "0" + hex_str

		mod_str += hex_str

	return mod_str



if __name__ == "__main__":

	print("--------------------------------------------------------------------------")
	print("EXECUTING TASK 1")
	print("--------------------------------------------------------------------------\n")

	# read in the plain text
	plain_text = readfile('mustang.bmp')

	# open a file to write encrypted output to
	output_file = open("encypted_ecb.bmp", "w+");

	# open a file to write encrypted output to
	output_file2 = open("encypted_cbc.bmp", "w+");

	#--------------------------------------------------------------------------
	# GENERATE THE KEY
	#
	print("\n--------------------------------------------------------------------------")
	print("START GENERATE THE KEY")

	# key for encoding
	key = os.urandom(16)
	cipher = AES.new(key, AES.MODE_ECB)
	print("Key: " + str(key))

	print("\nEND GENERATE THE KEY")
	#
	#--------------------------------------------------------------------------
	# DOING ECB ENCRYPTION
	print("--------------------------------------------------------------------------")
	print("START ECB ENCRYPTION")

	# loop through every plain text block to encrypt
	for block in plain_text:
		cipher_text.append(encrypt(block, cipher))
		
	# write all the data we just accumulated
	write_encrypted_data(cipher_text, output_file)

	print("\nEND ECB ENCRYPTION")
	#
	#--------------------------------------------------------------------------
	# DOING CBC ENCRYPTION
	print("--------------------------------------------------------------------------")
	print("START CBC ENCRYPTION")

	# reset cipher text
	cipher_text = []
	# read in the plain text
	plain_text2 = readfile('mustang.bmp')

	# creates the iv
	iv = os.urandom(16)
	cipher_text.append(iv)
	prev = iv

	for block in plain_text2:
		cipher_text.append(encrypt(XOR(block, prev), cipher))
		prev = block

	# write all the data we just accumulated
	write_encrypted_data(cipher_text, output_file2)

	print("\nEND CBC ENCRYPTION")
	#
	#--------------------------------------------------------------------------
	print("--------------------------------------------------------------------------")
	print("CLOSING FILEDESCRIPTORS\n\n")

	output_file.close()
	output_file2.close()










