
import sys

def calculate_value(a, b, PVALUE):
	if b == 1:
		return a
	else:
		return (pow(a, b) % PVALUE)


if __name__ == "__main__":

	PVALUE = 37
	GVALUE = 5

	a = 4
	b = 3

	print("===============================================")
	print("TASK 1:  GVALUE 5   PVALUE 37")
	print("===============================================")

	print("Value of P: ", PVALUE)
	print("Value of G: ", GVALUE)
	print("")

	print("Alice private key a: ", a)
	print("Bob private key b: ", b)
	print("")

	a_key = calculate_value(GVALUE, a, PVALUE)
	print("The a_key is: ", a_key)
	b_key = calculate_value(GVALUE, b, PVALUE)
	print("The b_key is: ", b_key)
	print("")

	alice_key = calculate_value(b_key, a, PVALUE)
	print("Secret key for alice: ", alice_key)

	bob_key = calculate_value(a_key, b, PVALUE)
	print("Secret key for bob: ", bob_key)
	print("")

	print("===============================================")
	print("TASK 1:  REAL LIFE NUMBERS")
	print("===============================================")

	PVALUE = 0xB10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371
	GVALUE = 0xA4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5

	print("Value of P: ", PVALUE)
	print("Value of G: ", GVALUE)
	print("")

	print("Alice private key a: ", a)
	print("Bob private key b: ", b)
	print("")

	a_key = calculate_value(GVALUE, a, PVALUE)
	print("The a_key is: ", a_key)
	b_key = calculate_value(GVALUE, b, PVALUE)
	print("The b_key is: ", b_key)
	print("")

	alice_key = calculate_value(b_key, a, PVALUE)
	print("Secret key for alice: ", alice_key)

	bob_key = calculate_value(a_key, b, PVALUE)
	print("Secret key for bob: ", bob_key)
	print("")

	if bob_key == alice_key:
		print("KEYS MATCH")
	else:
		print("KEY DON'T MATCH")
	print("")



































