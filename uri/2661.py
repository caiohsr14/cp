import math

x = int(input())
c = 0
r = int(math.sqrt(x))
k = 2

while x > 1 and k <= r:
	if x % k == 0:
		c += 1
		while x % k == 0:
			x = int(x/k)
	k += 1

if x > 1:
	c += 1

print (int(math.pow(2, c)) - c - 1)