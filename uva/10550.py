s = [int(x) for x in input().split()]
while s != [0] * 4:
	d = s[0] - s[1] if s[0] >= s[1] else 40 - s[1] + s[0]
	d += s[2] - s[1] if s[1] <= s[2] else 40 - s[1] + s[2]
	d += s[2] - s[3] if s[2] >= s[3] else 40 - s[3] + s[2]
	print(1080 + d * 9)
	s = [int(x) for x in input().split()]
