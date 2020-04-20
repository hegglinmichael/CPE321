# Author: Michael Hegglin
# Due Date 4 - 27 - 2020

import os

#--------------------------------------------------------------------
# START PART 1

# Description:
#  method xors two strings of the same length together
#  if strings aren't the same length an error is thrown
#
def xor_str(str1, str2):
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

# END PART 1
#--------------------------------------------------------------------
# START PART 2

def one_time_pad_txt(filename):

	key = ""
	original_txt = ""
	cipher_txt = ""
	new_originals = ""
	output_file = "ciphertext.txt"

	plain_txt = open(filename, "r")
	lines = plain_txt.readlines()
	plain_txt.close()

	write_to = open(output_file, "w+")

	for line in lines:
		original_txt += line

	key = os.urandom(len(original_txt))
	mod_str = xor_str(key, original_txt)
	write_to.write(mod_str.strip().decode("hex"))

	print("\nBack to plain text:")

	write_to.seek(0)
	lines = write_to.readlines()

	for line in lines:
		cipher_txt += line

	new_originals = xor_str(cipher_txt, key)

	if new_originals != None: 
		new_originals = new_originals.decode("hex")
	
	print(new_originals)
	write_to.close()

# END PART 2
#--------------------------------------------------------------------
# START PART 3

def one_time_pad_bmp(bmp1, bmp2):

	key1 = ""
	key2 = ""
	original_txt1 = ""
	original_txt2 = ""

	ct1 = ""
	ct2 = ""
	no1 = ""
	no2 = ""

	of1 = "ciphertext1.bmp"
	of2 = "ciphertext2.bmp"
	to1 = "to1.bmp"
	to2 = "to2.bmp"

	head1 = ""
	head2 = ""

	map1 = open(bmp1, "r")
	lines1 = map1.readlines()
	map1.close()

	map2 = open(bmp2, "r")
	lines2 = map2.readlines()
	map2.close()

	wt1 = open(of1, "w+")
	wt2 = open(of2, "w+")

	head1 = lines1[0][0:39]
	head2 = lines2[0][0:39]

	for line in lines1:
		original_txt1 += line

	for line in lines2:
		original_txt2 += line

	key1 = os.urandom(len(original_txt1))
	key2 = os.urandom(len(original_txt2))

	mod_str1 = xor_str(key1, original_txt1)
	mod_str2 = xor_str(key2, original_txt2)

	#print(mod_str1.decode("hex"))

	wt1.write(head1)
	wt1.write(mod_str1.decode("hex"))
	wt2.write(head2)
	wt2.write(mod_str2.decode("hex"))

	print("Images ready for manual checking!")

	wt1.seek(39, 0)
	wt2.seek(39, 0)
	lines1 = wt1.readlines()
	lines2 = wt2.readlines()

	for line in lines1:
		ct1 += line

	for line in lines2:
		ct2 += line

	no1 = xor_str(ct1, key1)
	no2 = xor_str(ct2, key2)

	if no1 != None: 
		no1 = no1.decode("hex")

	if no2 != None: 
		no2 = no2.decode("hex")
	
	wt1.close()
	wt2.close()

	testout1 = open(to1, "w+")
	testout1.write(no1);
	testout1.close()

	testout2 = open(to2, "w+")
	testout2.write(no2);
	testout2.close()

# END PART 3
#--------------------------------------------------------------------
# START PART 4

def one_time_pad_bmp_4(bmp1, bmp2):

	key1 = ""
	original_txt1 = ""
	original_txt2 = ""

	ct1 = ""
	ct2 = ""
	no1 = ""

	of1 = "ciphertext1.bmp"
	of2 = "ciphertext2.bmp"
	to = "to.bmp"

	head1 = ""
	head2 = ""

	map1 = open(bmp1, "r")
	lines1 = map1.readlines()
	map1.close()

	map2 = open(bmp2, "r")
	lines2 = map2.readlines()
	map2.close()

	wt1 = open(of1, "w+")
	wt2 = open(of2, "w+")

	head1 = lines1[0][0:39]
	head2 = lines2[0][0:39]

	for line in lines1:
		original_txt1 += line

	for line in lines2:
		original_txt2 += line

	key1 = os.urandom(len(original_txt1))

	mod_str1 = xor_str(key1, original_txt1)
	mod_str2 = xor_str(key1, original_txt2)

	#print(mod_str1.decode("hex"))

	wt1.write(head1)
	wt1.write(mod_str1.decode("hex"))
	wt2.write(head2)
	wt2.write(mod_str2.decode("hex"))

	print("Images ready for manual checking!")

	wt1.seek(39, 0)
	wt2.seek(39, 0)
	lines1 = wt1.readlines()
	lines2 = wt2.readlines()

	for line in lines1:
		ct1 += line

	for line in lines2:
		ct2 += line

	no1 = xor_str(ct1, ct2)

	if no1 != None: 
		no1 = no1.decode("hex")
	
	wt1.close()
	wt2.close()

	together = open(to, "w+")
	together.write(head1)
	together.write(no1);
	together.close()

# END PART 4
#--------------------------------------------------------------------

if __name__ == "__main__":

	test_file = "plain_text.txt"
	bt_map1 = "cp-logo.bmp"
	bt_map2 = "mustang.bmp"

	print("--------------------------------------------------------------------")
	print("START PART 1\n")

	print(xor_str("Darlin dont you go","and cut your hair!"))

	print("\nEND PART 1")
	print("--------------------------------------------------------------------")
	print("START PART 2\n")

	one_time_pad_txt(test_file)

	print("\nEND PART 2")
	print("--------------------------------------------------------------------")
	print("START PART 3\n")

	one_time_pad_bmp(bt_map1, bt_map2)

	print("\nEND PART 3")
	print("--------------------------------------------------------------------")
	print("START PART 4\n")

	one_time_pad_bmp_4(bt_map1, bt_map2)

	print("\nEND PART 4")
	print("--------------------------------------------------------------------")

