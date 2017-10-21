k = int(input())
while k != 0:
	n, m = [int(x) for x in input().split()]
	for i in range(k):
		x, y = [int(x) for x in input().split()]
		if x == n or y == m:
			print("divisa")
		elif x > n:
			print("NE" if y > m else "SE")
		else:
			print("NO" if y > m else "SO")
	k = int(input())
