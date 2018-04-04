s = input()
while s != "Game Over":
	r = [0] * 22
	a = 0
	i = 0
	for c in s.split():
		if c == 'X':
			r[i] = 12
		elif c == '/':
			r[i] = 11
		else:
			r[i] = int(c)
		a += r[i]
		i += 1
	for i in range(len(r)):
		if r[i] == 12:
			b = r[i+1] if r[i+1] != 12 else 10
			c = r[i+2] if r[i+2] < 11 else 10 - b if r[i+2] != 12 else 10
			a += b + c - 2
		elif r[i] == 11:
			b = r[i+1] if r[i+1] != 12 else 10
			a += b - r[i-1] - 1
	print(a)
	s = input()
