from itertools import permutations
for i in range(int(input())):
	perms = permutations(str(input()))
	perms = list(perms)
	perms.sort()
	prev = "  "	
	for j in perms:
		cur = ''.join(j)
		if (cur != prev):
			print (cur)
		prev = cur
	print ()