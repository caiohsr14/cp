from operator import add

pawn = [(1, 1), (1, -1)]
pawnB = [(-1, 1), (-1, -1)]
knight = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
topkek = [(0, -1), (0, 1), (1, 0), (-1, 0)]
full = diag + topkek

while True:
	try:
		z = {}
		m = 0
		s = input().split('/')
		for i in range(8):
			j = 0
			for c in s[i]:
				if not c.isdigit():
					z[(i, j)] = c
					j += 1
				else:
					for n in range(int(c)):
						z[(i, j)] = 0
						m += 1
						j += 1
		for i in range(8):
			for j in range(8):
				c = z[(i, j)]
				if c == 'k' or c == 'K':
					for v in full:
						f = tuple(map(add, (i, j), v))
						if f in z and z[f] == 0:
							z[f] = 1
							m -= 1
				if c == 'n' or c == 'N':
					for v in knight:
						f = tuple(map(add, (i, j), v))
						if f in z and z[f] == 0:
							z[f] = 1
							m -= 1
				if c == 'p':
					for v in pawn:
						f = tuple(map(add, (i, j), v))
						if f in z and z[f] == 0:
							z[f] = 1
							m -= 1
				if c == 'P':
					for v in pawnB:
						f = tuple(map(add, (i, j), v))
						if f in z and z[f] == 0:
							z[f] = 1
							m -= 1
				if c == 'q' or c == 'Q':
					for v in full:
						f = tuple(map(add, (i, j), v))
						while f in z and isinstance(z[f], int):
							if z[f] == 0:
								z[f] = 1
								m -= 1
							f = tuple(map(add, f, v))
				if c == 'b' or c == 'B':
					for v in diag:
						f = tuple(map(add, (i, j), v))
						while f in z and isinstance(z[f], int):
							if z[f] == 0:
								z[f] = 1
								m -= 1
							f = tuple(map(add, f, v))
				if c == 'r' or c == 'R':
					for v in topkek:
						f = tuple(map(add, (i, j), v))
						while f in z and isinstance(z[f], int):
							if z[f] == 0:
								z[f] = 1
								m -= 1
							f = tuple(map(add, f, v))
		print(m)
	except EOFError:
		break
