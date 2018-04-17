def main():
	a = []
	s = input()
	while s != "#":
		a += s.split()
		s = input()
	g = 0
	for i in range(len(a)):
		i -= g
		if i > len(a) - 2:
			break
		c = a[i]
		d = False
		h = [j for j in a[i+1:] if len(c) == len(j)]
		for f in h:
			if sorted(f.lower()) == sorted(c.lower()):
				a.remove(f)
				d = True
		if d:
			a.remove(c)
			g += 1
	a.sort()
	for c in a:
		print(c)

if __name__ == "__main__":
	main()
