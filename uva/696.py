s = [int(x) for x in input().split()]
while s != [0] * 2:
	n = int((s[0] * s[1] + 1) / 2)
	if s[0] < 2 or s[1] < 2:
		n = s[0] * s[1]
	elif s[0] == 2:
		if s[1] < 4:
			n = 4
		else:
			n = int(s[1]/4)*4 + (s[1]%4*2 if s[1]%4 < 3 else 4 if s[1]%4 == 3 else 0)
	elif s[1] == 2:
		n = 4 if s[0] == 3 else int(s[0]/4)*4 + (s[0]%4*2 if s[0]%4 < 3 else 4 if s[0]%4 == 3 else 0)
	print(n, "knights may be placed on a", s[0], "row", s[1], "column board.")
	s = [int(x) for x in input().split()]
