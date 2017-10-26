s = 0
for i in range(int(input())):
	z = input().split()
	if len(z) > 1:
		s += int(z[1])
	else:
		print(s)
