s = input()
while s != "0 0 0 0 0":
	s = [int(x) for x in s.split()]
	n = sorted(s)
	z = []
	m = -1
	for i in range(5):
		z.append(n.index(s[i]))
	b = sorted(z[3:])
	if b[1] == 4:
		m = 1 if b[0] == 3 else s[z.index(1)] if b[0] == 2 else s[z.index(3)]
	elif b[1] == 3 and b[0] == 2:
		m = s[z.index(1)]
	while m in s:
		m += 1
	print(m if m < 53 else -1)
	s = input()
