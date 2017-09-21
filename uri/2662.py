scales = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
gaps = [2, 2, 1, 2, 2, 2, 1]
n = set()

for i in range(int(input())):
	n.add((int(input()) - 1) % 12)

scale = -1
for i in range(len(scales)):
	af = True
	f = i
	ac = [f]
	for j in gaps:
		f += j
		ac.append(f%12)
	for j in n:
		if j not in ac:
			af = False
			break
	if af:
		scale = i
		break

if af:
	print(scales[scale])
else:
	print("desafinado")