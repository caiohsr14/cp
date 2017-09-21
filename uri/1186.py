if (input() == "M"):
	m = 0
	x = 0
	for i in range(12):
		for j in range(12):
			n = float(input())
			if (i + j > 11):
				m += n
				x += 1
	print(("{0:.1f}".format(m/x)))
else:
	m = 0
	for i in range(12):
		for j in range(12):
			n = float(input())
			if (i + j > 11):
				m += n
	print(("{0:.1f}".format(m)))