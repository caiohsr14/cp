#TLE
from sys import stdin, stdout
t = [[0, -1], [0, 1], [1, 0], [-1, 0]]
y = [1, 2, 0]
p = {'S': 0, 'R': 1, 'P': 2}
e = ['S', 'R', 'P']

def main():
	for i in range(int(stdin.readline())):
		if i > 0:
			stdout.write("\n")
		a, b, c = [int(x) for x in stdin.readline().strip().split()]
		z = [None, None]
		z[0] = [f[:] for f in [[None] * 102] * 102]
		z[1] = [f[:] for f in [[None] * 102] * 102]
		for j in range(a):
			k = 0
			for l in list(stdin.readline().strip()):
				z[0][j][k] = p[l]
				k += 1
		q = 0
		o = True
		for j in range(c):
			q = j + 1
			for k in range(a):
				for m in range(b):
					for v in range(4):
						g = k + t[v][0]
						h = m + t[v][1]
						if (g < 0 or g >= a or h < 0 or h >= b):
							continue
						o = False
						az = z[j&1][g][h]
						aw = z[j&1][k][m]
						if az == y[aw]:
							z[(j+1)&1][k][m] = az
							break
						else:
							z[(j+1)&1][k][m] = aw
		q = 0 if o else q
		for j in range(a):
			s = ""
			for k in range(b):
				s += e[z[q&1][j][k]]
			stdout.write(s + "\n")

if __name__ == "__main__":
	main()
