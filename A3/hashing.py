#  Author: Michael Hegglin
#  Date: 05-11-2020
#  Title: Assignment #3

import matplotlib.pyplot as plt 
from nltk.corpus import words
from hashlib import sha256
import bcrypt
import base64
import time
import sys
import re

user_passwd = {}
user_times = {}

size_to_time = {}
size_to_num_inputs = {}

'''

TASK 1

********************************************************************************
********************************************************************************
START T1 FUNCTIONS
'''

# Description
#   Hash function that hashes a string using
#   sha256 and outputs the value as a hexidecimal number
def hash_arb_input(str_input):
  print("  " + str(sha256(str_input).hexdigest()))

# Description
#   This function gets a certain number of the 
#   first few bits from the hash, and returns
#   the first few bits as a string
def get_trunc_hash(str_input, num):
  hash_str = str(sha256(str_input).hexdigest())
  fin = "{0:256b}".format(int(hash_str, 16))
  return fin[0:num]

def find_collisions_helper(num):
  str1 = "a".encode("ascii")
  count = 0.0
  temp = ""

  trunc_hash = get_trunc_hash(str1, num)

  for word in set(words.words()):
    word = word.encode("ascii")
    count += 1
    temp = get_trunc_hash(word, num)

    if temp == trunc_hash:
      print("FOUND COLLISION: " + str(num))
      size_to_num_inputs[num] = count
      break

# Description
#   Finds collision of trunc part of a hash
def find_collisions():
  
  for i in range(8, 51, 2):
    start = time.time()
    find_collisions_helper(i)
    end = time.time()
    size_to_time[i] = end - start

  print(size_to_num_inputs)
  print(size_to_time)

# Description
#   Plots the graphs for part c
def plot_graphs(data, x_t, y_t):
  x = []
  y = []

  for key in data.keys():
    x.append(key)
    y.append(data[key])

  plt.plot(x, y)
  plt.xlabel(x_t)
  plt.ylabel(y_t)
  plt.title('Size To Inputs')
  plt.show()

'''
END T1 FUNCTIONS
********************************************************************************
********************************************************************************

TASK 2

********************************************************************************
********************************************************************************
START T2 FUNCTIONS
'''

# Description
#   Nicely prints out the broken apart hash
#   for each user
def print_comb_str(user, rounds, value, salt):
  print("\n---------------------------------------------\n")
  print("User: ", user)
  print("Hash: ", value)
  print("Salt: ", salt)

# Description:
#   Encrypts a string by hashing so it can be returned to
#   compare to the hashes in the shadow.do
def encrypt_it(str_rand, num, salt):

  temp_salt = bcrypt.gensalt(rounds=num)

  hashed = bcrypt.hashpw(str_rand, salt)
  return hashed

# Description
#   This function test all the words in the 
#   words ntlk library.  It then compares them to 
#   to the hashed password we don't know
def decrypt_it_helper(user, rounds, bcrypt_output, salt):

  for word in words.words():
    word = word.encode('utf-8')
    temp_hash = encrypt_it(word, rounds, salt)

    if temp_hash == bcrypt_output:
      print("FOUND PASSWORD: ", word)
      user_passwd[user] = word
      break


# Description
#   This method is the bases for all
#   other decryption.  It parses aruments
#   then sends the args to be decrypted
def decrypt_it(user, comb_str):
  rounds = None
  rounds = int(comb_str[4:6])
  salt = comb_str[0:29]

  # missing_padding = len(salt) % 4
  # if missing_padding != 0:
  #   salt += b'='* (4 - missing_padding)

  # missing_padding = len(salt) % 4
  # salt = str(salt)
  # salt = base64.b64decode(salt)

  print_comb_str(user, rounds, comb_str, salt)

  start = time.time()
  decrypt_it_helper(user, rounds, comb_str, salt)
  end = time.time()
  user_times[user] = end - start


'''
END T2 FUNCTIONS
********************************************************************************
********************************************************************************
'''

if __name__ == "__main__":

  if sys.argv[1] == "1":

    print("\nTASK 1\n")
    print("***************************************************")
    print("***************************************************")
    print("START PART A\n")

    arb_input_a = "hello".encode('ascii')
    hash_arb_input(arb_input_a)


    print("\nEND PART A")
    print("---------------------------------------------------")
    print("START PART B\n")

    arb_input_b1 = "This is just an input for testing".encode('ascii')
    arb_input_b2 = "This is kust an input for testing".encode('ascii')
    hash_arb_input(arb_input_b1)
    hash_arb_input(arb_input_b2)
    print()

    arb_input_b3 = "banana".encode('ascii')
    arb_input_b4 = "canana".encode('ascii')
    hash_arb_input(arb_input_b3)
    hash_arb_input(arb_input_b4)
    print()

    arb_input_b5 = "b".encode('ascii')
    arb_input_b6 = "c".encode('ascii')
    hash_arb_input(arb_input_b5)
    hash_arb_input(arb_input_b6)


    print("\nEND PART B")
    print("---------------------------------------------------")
    print("START PART C\n")

    # print("  " + get_trunc_hash("apples".encode("ascii"), 8))
    find_collisions()
    plot_graphs(size_to_time, "Digest Size", "Collision Time")
    plot_graphs(size_to_num_inputs, "Digest Size", "Number Of Inputs")


    print("\nEND PART C")
    print("***************************************************")
    print("***************************************************")

  elif sys.argv[1] == "2": 

    shadow = {"Bilbo":b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq',
              "Gandalf":b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC",
              "Thorin":b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q",
              "Fili":b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm",
              "Kili":b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im",
              "Balin":b"$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom",
              "Dwalin":b"$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be",
              "Oin":b"$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK",
              "Gloin":b"$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q",
              "Dori":b"$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq",
              "Nori":b"$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12",
              "Ori":b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O",
              "Bifur":b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK",
              "Bofur":b"$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O",
              "Durin":b"$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"}
    
    print("\nTASK 2\n")
    print("***************************************************")
    print("***************************************************")
    print("START PART A\n")

    for user in shadow:
      decrypt_it(user, shadow[user])

    print(user_passwd)
    print(user_times)
    # encrypt_it("apples".encode("ascii"), 10)

    print("\nEND PART A")
    print("***************************************************")
    print("***************************************************")




















