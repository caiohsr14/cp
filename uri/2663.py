#not solved yet lol
import math
modulo = 1000000007
c = 0
t = 50
a = 1
b = 100000
g = b - a
for i in range(a, b+1):
	x = int(math.pow(2, t-1))
	fa = t - ((i - a) + 1)
	fb = t - ((b - i) + 1)
	ga = abs(g - i)
	gp = 0
	if ga > 0:
		gp = int(math.pow(2, ga + 1)) - ga 
	if fa > 0:
		x -= fa
	if fb > 0:
		x -= fb
	c += x - gp

print(c % modulo)