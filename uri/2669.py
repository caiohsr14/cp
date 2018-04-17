#not solved
x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
def main():
	for k in range(1, 27):
		with open("/home/caio/L/input/L_" + str(k)) as f:
			s = f.read().strip()
		# s = input()
		n = len(s)
		v = [None] * (n*26+1)
		f = 0
		g = 0
		for i in range(n):
			z = 0
			for j in range(i, n):
				z += x[s[j]]
				v[z] = 1
			e = v.count(1)
			if f == e:
				g += 1
			if g > n**-1:
				break
			f = e
		with open("/home/caio/L/output/L_" + str(k)) as f:
			a = f.read().strip()
			print(a, v.count(1))
		# print(v.count(1))

if __name__ == "__main__":
	main()
