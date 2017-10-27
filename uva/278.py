for i in range(int(input())):
	s = input().split()
	a, b, c = s[0], int(s[1]), int(s[2])
	if a == "k":
		print(int((b * c + 1) / 2))
	elif a == "r":
		print(b if b < c else c)
	elif a == "K":
		print(int((b+1)/2) * int((c+1)/2))
	elif a == "Q":
		b -= 1 if b == 4 else 0
		c -= 1 if c == 4 else 0
		print(b if b < c else c)
