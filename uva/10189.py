from operator import add
n, m = [int(x) for x in input().split()]
f = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (1, 0), (-1, 0)]
d = 1
while n != 0 and m != 0:
	if d > 1:
		print()
	print("Field #" + str(d) + ":")
	z = {}
	for i in range(n):
		j = 0
		for c in list(input()):
			z[(i, j)] = c
			j += 1
	for i in range(n):
		s = ""
		for j in range(m):
			a = z[(i, j)]
			if a == '.':
				b = 0
				for v in f:
					c = tuple(map(add, (i, j), v))
					if c in z and z[c] == '*':
						b += 1
				z[(i, j)] = b
			s += str(z[(i, j)])
		print(s)
	d += 1
	n, m = [int(x) for x in input().split()]
