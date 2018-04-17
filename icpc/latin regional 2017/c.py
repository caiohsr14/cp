from collections import Counter
def main():
	k, n = [int(x) for x in input().split()]
	v = [int(x) for x in input().split()]
	c = Counter(v)
	x = Counter(c.values())
	f = sorted(x.items(), key=lambda x:x[1], reverse=True)
	if len(c) == k - 1 and f[0][0] == 1:
		a = list(sorted(set(v)))
		b = 1
		i = 0
		while i < len(a) and b == a[i]:
			b += 1
			i += 1
		if len(f) == 2 and f[1][1] == 1 and f[1][0] == 2:
			print("-" + str(list(c.keys())[list(c.values()).index(f[1][0])]), "+" + str(b))
		elif len(f) == 1:
			print("+" + str(b))
		else:
			print("*")
	elif len(c) == k:
		if len(f) == 2 and f[1][1] == 1:
			if abs(f[1][0] - f[0][0]) == 1:
				if f[1][0] > f[0][0]:
					print("-" + str(list(c.keys())[list(c.values()).index(f[1][0])]))
				else:
					print("+" + str(list(c.keys())[list(c.values()).index(f[1][0])]))
			else:
				print("*")
		elif len(f) == 3 and f[1][1] == 1 and f[2][1] == 1:
			if f[0][1] == 1:
				f = sorted(x.items(), key=lambda x:x[0])
				l = f[0]
				f[0] = f[1]
				f[1] = l
			if abs(f[1][0] - f[0][0]) == 1 and abs(f[2][0] - f[0][0]) == 1:
				if f[1][0] > f[0][0]:
					print("-" + str(list(c.keys())[list(c.values()).index(f[1][0])]), "+" + str(list(c.keys())[list(c.values()).index(f[2][0])]))
				else:
					print("-" + str(list(c.keys())[list(c.values()).index(f[2][0])]), "+" + str(list(c.keys())[list(c.values()).index(f[1][0])]))
			else:
				print("*")
		else:
			print("*")
	else:
		print("*")

if __name__ == "__main__":
	main()
