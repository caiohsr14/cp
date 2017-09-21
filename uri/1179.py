def printArray(array, fold):
	for x in range(len(array)):
		print(fold + "[" + str(x) + "] = " + str(array[x]))

p = []
imp = []
for i in range(15):
	n = int(input())
	if (n%2 == 0):
		if (len(p) == 5):
			printArray(p, "par")
			p = []
		p.append(n)
	else:
		if (len(imp) == 5):
			printArray(imp, "impar")
			imp = []
		imp.append(n)
printArray(imp, "impar")
printArray(p, "par")