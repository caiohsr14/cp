from collections import OrderedDict
l, c = [int(x) for x in input().split()]
v = []
sL = []
sC = []
un = set()
k = {}

def update(pair, value):
	for i in range(l):
		for j in range(c):
			if (v[i][j] == pair):
				sL[i] -= value
				sC[j] -= value

for i in range(l):
	x = input().split()
	v.append(x)
	for m in range(c):
		un.add(v[i][m])
	sL.append(int(x[c]))
sC = [int(x) for x in input().split()]

while(len(k) != len(un)):
	for i in range(l):
		u = set()
		n = 0
		for j in range(c):
			if (v[i][j] not in k):
				u.add(v[i][j])
				n += 1
		if (len(u) == 1):
			val = int(sL[i]/n)
			k[max(u)] = val
			update(max(u), val)
			break
	for j in range(c):
		u = set()
		n = 0
		for i in range(l):
			if (v[i][j] not in k):
				u.add(v[i][j])
				n += 1
		if (len(u) == 1):
			val = int(sC[j]/n)
			k[max(u)] = val
			update(max(u), val)
			break
k = OrderedDict(sorted(k.items()))
for k, v in k.items():
	print (k + " " + str(v))