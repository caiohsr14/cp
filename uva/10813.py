def winner(a, b):
	e, f = True, True
	for i in range(5):
		c, d = True, True
		for j in range(5):
			if a[b[i][j]]:
				c = False
			if a[b[j][i]]:
				d = False
		if c or d:
			break
		if a[b[i][i]]:
			e = False
		if a[b[i][4-i]]:
			f = False
	return c or d or e or f

for n in range(int(input())):
	z = [k[:] for k in [[0] * 5] * 5]
	x = [1] * 76
	x[0] = 0
	for i in range(5):
		l = 0
		for j in input().split():
			if i == 2 and l == 2:
				l += 1
			z[i][l] = int(j)
			l += 1
	w = True
	q = 1
	i = 0
	while i != 75:
		if w:
			for j in input().strip().split():
				x[int(j)] = 0
				i += 1
				if winner(x, z):
					w = False
				else:
					q += 1
		else:
			for j in input().strip().split():
				i += 1
	print("BINGO after", q, "numbers announced")
