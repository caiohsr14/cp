for i in range(int(input())):
	s, d = [int(x) for x in input().split()]
	a = (s + d) / 2
	if a.is_integer():
		b = s - a
		if b >= 0:
			print(int(a), int(b))
		else:
			print("impossible")
	else:
		print("impossible")
