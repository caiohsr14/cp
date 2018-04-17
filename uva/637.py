n = int(input())
while n != 0:
	s = list(range(1, n + 1))
	for i in range(((n - 1)//4 + 1) * 4 - n):
		s.append("Blank")
	print("Printing order for", n, "pages:")
	x = 1
	f = True
	for i in range(len(s)//2):
		d = (i + 1) * -1 if f else i
		b = i if f else (i + 1) * -1 
		if s[d] != "Blank" or s[b] != "Blank":
			print("Sheet " + str(x) + ", " + ("front: " if f else "back : ") + str(s[d]) + ", " + str(s[b]))
		x += 0 if f else 1
		f = not f
	n = int(input())
