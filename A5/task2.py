from Crypto.Cipher import AES
import urllib
import sys
import os

block_size = 16

def pad_string(s):
    return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

def unpad_string(s):
    return s[:-ord( s[len(s) - 1:] )]

def encrypt(text, key):
	return key.encrypt(text)

def decrypt(text, key):
	return key.decrypt(text)

def input_to_blocks(text, iv):
	text_blocks = []
	temp = ""

	l = len(text)
	l += 1

	for i in range(l):
		if i % 16 == 0 and temp != "":
			text_blocks.append(temp)
			temp = ""

		if i == len(text):
			break

		temp += text[i]

	print("blocks:  ")
	print(text_blocks)
	print("\n")
	return text_blocks

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

	return mod_str.decode("hex")

# Description
#	submit method as specified in A5
#
def submit(key, iv):
	cipher_text = []
	total_cipher = ""

	encode_str = "userid=456;userdata="
	txt = raw_input("Enter something:")

	encode_str += txt
	encode_str += ";session-id=31337"

	encode_str = pad_string(encode_str)
	print(encode_str)
	blocks = input_to_blocks(encode_str, iv)

	cipher = AES.new(key, AES.MODE_ECB)
	prev = iv

	for block in blocks:
		t = encrypt(block, cipher)
		t = encrypt(XOR(block, prev), cipher)
		cipher_text.append(t)
		prev = t

	# print(cipher_text)
	# for i in cipher_text:
	# 	total_cipher += i

	return cipher_text
	# return total_cipher

# Description
#	verify method as specified in verify
#
def verify(key, iv, encoded_str):
	total_str = ""

	cipher = AES.new(key, AES.MODE_ECB)

	for i in range(len(encoded_str) - 1, -1, -1):
		t = decrypt(encoded_str[i], cipher)

		if (i == 0):
			t = XOR(t, iv)
		else:
			t = XOR(t, encoded_str[i - 1])

		total_str = t + total_str

	print("DECODED")
	print(total_str)


	if "admin=true" in decrypted_cipher:
		return True
	else:
		return False


if __name__ == "__main__":

	print("--------------------------------------------------------------------------")
	print("EXECUTING TASK 2")
	print("--------------------------------------------------------------------------\n")
	print("\n--------------------------------------------------------------------------")
	print("START GENERATE THE KEY, IV")

	# key for encoding
	key = os.urandom(block_size)
	print("Key: " + str(key))

	# creates the iv
	iv = os.urandom(block_size)
	print("iv: " + iv)

	print("\nEND GENERATE THE KEY, IV")
	print("--------------------------------------------------------------------------")
	print("START SUBMIT\n")

	cipher_text = submit(key, iv)
	print("CIPHER TEXT BELOW")
	print(cipher_text)

	print("\nEND SUBMIT")
	print("--------------------------------------------------------------------------")
	print("START VERIFY\n")

	tf = verify(key, iv, cipher_text)
	if(tf):
		print("TRUE")
	else:
		print("FALSE")

	print("\nEND VERIFY")
	print("--------------------------------------------------------------------------\n")











