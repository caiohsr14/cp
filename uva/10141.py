n, p = [int(x) for x in input().split()]
rfp = 1
while n != 0 and p != 0:
	if rfp > 1:
		print()
	best = ""
	m, c = -1, -1.0
	for i in range(n):
		input()
	for i in range(p):
		name = input()
		a = input().split()
		d, r = float(a[0]), int(a[1])
		for j in range(int(r)):
			input()
		if r > m:
			best = name
			m = r
			c = d
		elif r == m and d < c:
			best = name
			c = d
	print("RFP #", rfp, sep = '')
	print(best)
	n, p = [int(x) for x in input().split()]
	rfp += 1
