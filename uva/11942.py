print("Lumberjacks:")
for i in range(int(input())):
	v = [int(x) for x in input().split()]
	print("Ordered" if v == sorted(v) or v == sorted(v, reverse=True) else "Unordered")
