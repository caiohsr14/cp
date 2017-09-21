n, r = [int(x) for x in input().split()]
z = {}
c = {}
for i in range(n):
	a = input().split()
	z[a[0]] = a[1:]
	c[a[0]] = []
	if int(a[3]) > 1:
		for j in range(0, int(a[3]) - 1):
			cj = int(a[7 + j*2]) - int(a[6 + j*2]) + 1
			c[a[0]].append(cj)
	c[a[0]].append(int(a[2]))
	for j in range(int(a[3]) - 2, -1, -1):
		c[a[0]][j] *= c[a[0]][j+1]
	cz = int(a[1])
	x = 0
	for j in range(4, len(a), 2):
		cz -= c[a[0]][x] * int(a[j])
		x += 1
	c[a[0]].append(cz)

for i in range(r):
	a = input().split()
	t = c[a[0]]
	v = [int(x) for x in a[1:]]
	f = t[-1]
	for i in range(len(v)):
		f += v[i] * t[i]
	print(a[0] + str(v), "=", f)