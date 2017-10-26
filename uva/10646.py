for i in range(int(input())):
	p = input().split()
	y = -1
	for j in range(3):
		x = int(p[-26][0]) if p[-26][0].isdigit() else 10
		y += x
		p = p[:-(36-x)] + p[-25:]
	print("Case", str(i+1) + ":", p[y])
