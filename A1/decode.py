
import sys
import math

# mapping of normal frequencies of letters in english language
char_freq_mapping = {"a": 8.17, "b": 1.49, "c": 2.20, "d": 4.25, "e": 12.70, "f": 2.23, 
					 "g": 2.02, "h": 6.09, "i": 6.97, "j": 0.15, "k": 1.29, "l": 4.03, 
					 "m": 2.41, "n": 6.75, "o": 7.51, "p": 1.93, "q": 0.10, "r": 5.99,
					 "s": 6.33, "t": 9.36, "u": 2.76, "v": 0.98, "w": 2.56, "x": 0.15, 
					 "y": 1.99, "z": .08}

helper = {"a": [], "b": [], "c": [], "d": [], "e": [], "f": [], 
		  "g": [], "h": [], "i": [], "j": [], "k": [], "l": [], 
		  "m": [], "n": [], "o": [], "p": [], "q": [], "r": [],
		  "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], 
		  "y": [], "z": []}

alphebet = "abcdefghijklmnopqrstuvwxyz"

input_char_freq_mapping = {}
tuple_mapping = {}

text = ""

def count_input_char_freq(filename):
	total = 0

	with open(filename) as encrypted_file:
		lines = encrypted_file.readlines()
		encrypted_file.close()

	for line in lines:
		line = line.lower()
		for char in line:
			if char in alphebet:
				if char in input_char_freq_mapping:
					total += 1
					input_char_freq_mapping[char] = input_char_freq_mapping[char] + 1
				else:
					total += 1
					input_char_freq_mapping[char] = 1

	for char in input_char_freq_mapping:
		input_char_freq_mapping[char] = (input_char_freq_mapping[char] / total) * 100

#  Description:
#		prints out all possible combinations
#		using a brute force method
def caesar(input_file_name):
	lines = ""

	with open(input_file_name) as encrypted_file:
		lines = encrypted_file.readlines()

	for i in range(26):
		print("KEY = " + str(i) + "--------------------------------------\n")
		guess_str = ""

		for line in lines:
			line = line.lower()

			for char in line:
				if char in alphebet:
					pos = alphebet.find(char) - i
					pos = pos % 26
					guess_str += alphebet[pos]
				else:
					guess_str += char

		print(guess_str)
		print("\n\n")


def mono_alphebetic(input_file_name):
	count_input_char_freq(input_file_name)

	mapping = {}
	keys = []
	values = []
	lines = ""
	guess_str = ""

	with open(input_file_name) as encrypted_file:
		lines = encrypted_file.readlines()
		encrypted_file.close()

	for i in sorted(input_char_freq_mapping, key=input_char_freq_mapping.get, reverse=True):
		print(i, input_char_freq_mapping[i])
		keys.append(i)

	print("next------")

	for i in sorted(char_freq_mapping, key=char_freq_mapping.get, reverse=True):
		print(i, char_freq_mapping[i])
		values.append(i)

	for i in range(len(keys)):
		mapping[keys[i]] = values[i]

	# # mapping["x"] = "h"
	# mapping["l"] = "p"
	# mapping["f"] = "m"
	# # mapping["n"] = "g"
	# # mapping["g"] = "r"
	# mapping["j"] = "n"
	# # mapping["a"] = "w"
	# mapping["t"] = "j"
	# mapping["h"] = "h"
	# mapping["o"] = "w"
	# mapping["i"] = "b"
	# mapping["s"] = "i"
	# mapping["u"] = "y"
	# mapping["m"] = "c"
	# # mapping["w"] = "u"
	# mapping["r"] = "u"
	# mapping["c"] = "o"
	# mapping["p"] = "g"
	# # mapping["k"] = "t"
	# mapping["y"] = "s"
	# mapping["g"] = "l"
	# mapping["b"] = "f"
	# # mapping["d"] = "y"
	# # mapping["e"] = "z"

	print(mapping)

	for line in lines:
		line = line.lower()

		for char in line:
			if char in alphebet:
				guess_str += mapping[char]
			else:
				guess_str += char


	print(guess_str)

	# a = ""

	# for key in sorted(mapping, key=mapping.get):
	# 	print(mapping[key])
	# 	a += key

	# print(a)


def vigenere(input_file_name):

	key = "dbdubdfbf"
	key_len = len(key)

	index = 0
	lines = ""
	guess_str = ""

	with open(input_file_name) as encrypted_file:
		lines = encrypted_file.readlines()
		encrypted_file.close()


	for line in lines:
		for char in line:
			if char in alphebet:
				i = index % key_len
				unmodded = ord(char) - ord(key[i])
				modded = unmodded % 26

				temp_str = alphebet[modded]
				guess_str += temp_str
				index += 1
			else:
				guess_str += char

	print(guess_str)

if __name__ == "__main__":

	if len(sys.argv) < 3:
		print("Usage: python3 decode.py <flag> <encoded file>")
		print("\t-m: mono alphebetic decoder")
		print("\t-v: vigenere decoder")
		print("\t-c: caesar decoder")
	else:
		if sys.argv[1] == "-v":
			vigenere(sys.argv[2])

		elif sys.argv[1] == "-m":
			mono_alphebetic(sys.argv[2])

		elif sys.argv[1] == "-c":
			caesar(sys.argv[2])

	sys.exit(0)
