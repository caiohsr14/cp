from sys import stdin, stdout
def main():
	n = int(stdin.readline().strip()) - 1
	stdin.readline()
	while n >= 0:
		e = []
		f = []
		s = stdin.readline().strip()
		while s != "":
			f.append(s)
			s = stdin.readline().strip()
		f.sort()
		for c in f:
			e.append(sorted(c.replace(' ', '')))
		l = len(f)
		for j in range(l-1):
			for k in range(j+1, l):
				if e[j] == e[k]:
					stdout.write(f[j] + " = " + f[k] + "\n")
		if n:
			stdout.write("\n")
		n -= 1

if __name__ == "__main__":
	main()
