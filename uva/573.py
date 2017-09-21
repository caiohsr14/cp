h, u, d, f = [int(x) for x in input().split()]
while h != 0:
	f = f * u / 100
	day = 1
	c = u
	while True:
		if c > h:
			print("success on day", day)
			break
		c -= d
		if c < 0:
			print("failure on day", day)
			break
		u -= f
		if u > 0:
			c += u
		else:
			print("failure on day", int(c/d) + 1 + day)
			break
		day += 1
	h, u, d, f = [int(x) for x in input().split()]