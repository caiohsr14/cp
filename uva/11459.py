for i in range(int(input())):
	a, b, c = [int(x) for x in input().split()]
	p = [1] * (a + 1)
	z = {}
	for j in range(b):
		s = [int(x) for x in input().split()]
		z[s[0]] = s[1]
	n = 1
	k = 0
	if a > 0:
		for j in range(c):
			p[n] += int(input())
			if p[n] in z:
				p[n] = z[p[n]]
			if p[n] >= 100:
				p[n] = 100
				k = c - j
				break
			n = n % a + 1
	else:
		k = c + 1
	for j in range(k - 1):
		input()
	for j in range(1, a+1):
		print("Position of player", j, "is", str(p[j]) + ".")
