import math
for i in range(int(input())):
	n = int(input())
	b = int(math.ceil((n-1)/2) * int(math.ceil(n/2)) + int(math.ceil((n-2)/2)))
	print (str(b*2+1))