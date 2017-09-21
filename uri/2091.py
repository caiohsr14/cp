from collections import Counter
while(int(input()) != 0):
	z = [int(f) for f in input().split()]
	x = Counter(z)
	for k, v in x.items():
		if (v % 2 != 0):
			print (k)
			break