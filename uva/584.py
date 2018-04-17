from sys import stdin, stdout
z = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '/': 11, 'X': 12}
stri = str
def main():
	s = stdin.readline().strip()
	while s != "Game Over":
		b = [0] * 22
		c, d, e = 0, 0, 0
		for a in s.split():
			if d > 17:
				if a == 'X':
					b[e] = 10
				elif a == '/':
					b[e] = 10 - b[e-1]
				else:
					b[e] = z[a]
			else:
				b[e] = z[a]
			c += b[e]
			d += 1 if b[e] != 12 else 2
			e += 1
		for i in range(21, -1, -1):
			if b[i] == 12:
				c += b[i+1] + b[i+2] - 2
				b[i] = 10
			elif b[i] == 11:
				c += b[i+1] - b[i-1] - 1
				b[i] = 10 - b[i-1]
		stdout.write(stri(c) + "\n")
		s = stdin.readline().strip()

if __name__ == "__main__":
	main()
