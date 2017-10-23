while True:
	try:
		n, b, h, w = [int(x) for x in input().split()]
		m = -1
		for i in range(h):
			p = int(input())
			a = [int(x) for x in input().split()]
			if p * n > b:
				continue
			for x in a:
				if n <= x:
					m = m if m > -1 and m < p * n else p * n
					break
		print(m if m > -1 else "stay home")
	except EOFError:
		break
