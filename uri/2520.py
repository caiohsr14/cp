while True:
	try:
		z = [int(f) for f in input().split()]
		i = 0
		a = [0, 0, 0, 0]
		for h in range(z[0]):
			x = [int(f) for f in input().split()]
			if (1 in x):
				a[0] = x.index(1)
				a[1] = i
			if (2 in x):
				a[2] = x.index(2)
				a[3] = i
			i += 1
		print (abs(a[0] - a[2]) + abs(a[1] - a[3]))
	except EOFError:
		break