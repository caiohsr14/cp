for i in range(int(input())):
	w = list(input())
	n = int(input()) - 39
	cipher = (chr((ord(c) - n) % 26 + 65) for c in w)
	print ("".join(cipher)) 