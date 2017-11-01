#TLE
from sys import stdin, stdout
def main():
	t = [[0, -1], [0, 1], [1, 0], [-1, 0]]
	for i in range(int(stdin.readline())):
		if i > 0:
			stdout.write("\n")
		a, b, c = stdin.readline().split()
		a = int(a)
		b = int(b)
		c = int(c)
		z = [f[:] for f in [[0] * 102] * 102]
		for j in range(a):
			k = 0
			for l in list(stdin.readline()):
				z[j][k] = l
				k += 1
		x = [f[:] for f in z]
		for j in range(c):
			o = True
			for k in range(a):
				for m in range(b):
					for v in range(4):
						g = k + t[v][0]
						h = m + t[v][1]
						if (g < 0 or g >= a or h < 0 or h >= b):
							continue
						if(x[g][h] == 'S' and x[k][m] == 'P'):
							z[k][m] = 'S'
							o = False
						elif(x[g][h] == 'P' and x[k][m] == 'R'):
							z[k][m] = 'P'
							o = False
						elif(x[g][h] == 'R' and x[k][m] == 'S'):
							z[k][m] = 'R'
							o = False
			if o:
				break
			x = [f[:] for f in z]
		for j in range(a):
			s = []
			for k in range(b):
				s.append(z[j][k])
			stdout.write("".join(s) + "\n")

if __name__ == "__main__":
	main()
