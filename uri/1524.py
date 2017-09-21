while True:
	try:
		n, k = [int(x) for x in input().split()]
		v = [int(x) for x in input().split()]
		r = 0
		ant = 0
		for i in v:
			if i == ant:
				r += 1
			ant = i
		x = n-k-r
		print (0 if x < 0 else x)
	except EOFError:
		break