n, m, c = [int(x) for x in input().split()]
s = 1

while (n != 0 and m != 0 and c != 0):
	x = 0
	a = -1
	d = {}
	z = [0]
	for i in range(n):
		f = int(input())
		z.append(f)
		d[i + 1] = False
	for i in range(m):
		f = int(input())
		d[f] = not d[f]
		if d[f]:
			x += z[f]
			a = max(a, x)
		else:
			x -= z[f]
	print("Sequence", s)
	if a > c:
		print("Fuse was blown.")
	else:
		print("Fuse was not blown.")
		print("Maximal power consumption was", a, "amperes.")
	print()
	n, m, c = [int(x) for x in input().split()]
	s += 1