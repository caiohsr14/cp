for i in range(int(input())):
	n = int(input())
	v = []
	w = []
	bag = [0] * 51
	bagW = [0] * 51
	for x in range(n):
		a, b = [int(c) for c in input().split()]
		v.append(a)
		w.append(b)
	for x in range(n):
		W = 50
		while (W - w[x] >= 0):
			if (bag[W] < (bag[W - w[x]] + v[x])):
				bag[W] = bag[W - w[x]] + v[x]
				bagW[W] = bagW[W - w[x]] + 1
			W -= 1
	ans = 50
	for x in range(49, 0, -1):
		if (bag[x] >= bag[ans]):
			ans = x
		else:
			break
	print (str(bag[ans]) + " brinquedos")
	print ("Peso: " + str(ans) + " kg")
	print ("sobra(m) " + str(n - bagW[ans]) + " pacote(s)")
	print ()