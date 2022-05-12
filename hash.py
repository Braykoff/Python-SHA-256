def lowestMultiple(multiple, greaterThan):
	current = 0
	while current < greaterThan:
		current += multiple
	return current

def splitIntoList(original, stringSize):
	new = []
	if len(original)%stringSize != 0:
		raise Exception("Length of string must be divisible by stringSize.")
		return
	while original != "":
		new.append(original[0:stringSize])
		original = original[stringSize:]
	return new

def xorAddBinary(binary):
	final = "0"*len(binary[0])

	for b in binary:
		l = list(final)
		for x in range(0, len(b)):
			if b[x] != final[x]:
				l[x] = "1"
			else:
				l[x] = "0"
		final = "".join(l)
	return final

def andAddBinary(binary):
	final = "1"*len(binary[0])

	for b in binary:
		l = list(final)
		for x in range(0, len(b)):
			if b[x] == "0":
				l[x] = "0"
		final = "".join(l)

	return final

def notBinary(binary):
	final = ""
	for b in binary:
		if b == "1":
			final += "0"
		else:
			final += "1"
	return final

def padBinary(binary):
	maxLength = 1
	for b in binary:
		if len(b) > maxLength:
			maxLength = len(b)
	
	padded = []

	for b in binary:
		padded.append(b.zfill(maxLength))

	return padded

def addBinary(binary): # with modulo 2^32
	final = list("0"*32)
	
	for b in binary:
		if len(b) > 32:
			b = b[len(b)-32:]
		elif len(b) < 32:
			b = b.zfill(32)

		carry = 0
		for c in range(len(b)-1, -1, -1):
			ones = carry + int(b[c]) + int(final[c])
			if ones == 1:
				final[c] = "1"
				carry = 0
			elif ones == 2:
				final[c] = "0"
				carry = 1
			elif ones == 3:
				final[c] = "1"
				carry = 1

	return "".join(final)

def rightRotate(string, amount):
	for _ in range(0, amount):
		last = string[len(string)-1]
		string = last + string
		string = string[0:len(string)-1]
	return string

def rightShift(string, amount):
	return ("0"*amount) + string[0:len(string)-amount]

def getNextWord(words):
	i = len(words)

	string1 = xorAddBinary([
		rightRotate(words[i-15], 7),
		rightRotate(words[i-15], 18),
		rightShift(words[i-15], 3)
	])

	string2 = xorAddBinary([
		rightRotate(words[i-2], 17),
		rightRotate(words[i-2], 19),
		rightShift(words[i-2], 10)
	])

	return addBinary([
		words[i-16],
		string1,
		words[i-7],
		string2
	])

def binaryToHex(binary):
	while len(binary)%4 != 0:
		binary = "0" + binary
	final = ""

	letters = ["a", "b", "c", "d", "e", "f"]

	for x in range(0, len(binary), 4):
		total = 0
		if binary[x] == "1":
			total += 8
		if binary[x+1] == "1":
			total += 4
		if binary[x+2] == "1":
			total += 2
		if binary[x+3] == "1":
			total += 1

		if total > 9:
			total = total-10
			final += letters[total]
		else:
			final += str(total)
	
	return final

def textToSha256(text):
	binary = "".join(format(ord(i), '08b') for i in text) + "1"
	length = "{0:08b}".format(len(binary)-1)

	l = lowestMultiple(512, len(binary)+len(length))
	binary += ("0" * (l - (len(binary)+len(length)))) + length
	binary = splitIntoList(binary, 512)
	
	hashes = [
		0x6a09e667,
		0xbb67ae85,
		0x3c6ef372,
		0xa54ff53a,
		0x510e527f,
		0x9b05688c,
		0x1f83d9ab,
		0x5be0cd19
	]

	roundConstants = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

	for x in range(0, len(hashes)):
		hashes[x] = "{0:08b}".format(int(hashes[x]))
	
	for k in range(0, len(roundConstants)):
		roundConstants[k] = "{0:08b}".format(int(roundConstants[k]))
		
	hashes = padBinary(hashes)
	roundConstants = padBinary(roundConstants)

	for chunk in binary:
		chunk = splitIntoList(chunk, 32)

		while len(chunk) % 64 != 0:
			chunk.append(getNextWord(chunk))

		a, b, c, d, e, f, g, h = hashes
		
		for i in range(0, 64):
			s1 = xorAddBinary([
				rightRotate(e, 6),
				rightRotate(e, 11),
				rightRotate(e, 25)
			])
			ch = xorAddBinary([
				andAddBinary([e, f]),
				andAddBinary([notBinary(e), g])
			])
			temp1 = addBinary([h, s1, ch, roundConstants[i], chunk[i]])
			s0 = xorAddBinary([
				rightRotate(a, 2),
				rightRotate(a, 13),
				rightRotate(a, 22)
			])
			maj = xorAddBinary([
				andAddBinary([a, b]),
				andAddBinary([a, c]),
				andAddBinary([b, c])
			])
			temp2 = addBinary([s0, maj])
			h = g
			g = f
			f = e
			e = addBinary([d, temp1])
			d = c
			c = b
			b = a
			a = addBinary([temp1, temp2])

		for x in range(0, 8):
			hashes[x] = addBinary([hashes[x], [a, b, c, d, e, f, g, h][x]])
		
	digest = ""
	for hash in hashes:
		digest += hash
	
	return binaryToHex(digest)
