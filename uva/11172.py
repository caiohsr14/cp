for i in range(int(input())):
	a, b = [int(x) for x in input().split()]
	print(">" if a > b else "<" if a < b else "=")