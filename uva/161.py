def main():
	s = input()
	f = []
	c = {}
	while s != "0 0 0":
		a = [int(x) for x in s.split()]
		for b in a:
			if b == 0:
				f.append(c)
				c = {}
			else:
				c[b] = b*2
		s = input()
	for a in f:
		b = max(a)
		t = a[b]
		while t < 18000:
			

if __name__ == "__main__":
	main()
