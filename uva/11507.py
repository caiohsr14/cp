l = int(input())
while l != 0:
	ds = input().split()
	r = "+x"
	for d in ds:
		if "y" in d:
			r = d if r == "+x" else "-" + d[1] if r == "-x" and d[0] == "+" else "+" + d[1] if r == "-x" else r if "z" in r else "-x" if r[0] == d[0] else "+x"
		elif "z" in d:
			r = d if r == "+x" else "-" + d[1] if r == "-x" and d[0] == "+" else "+" + d[1] if r == "-x" else r if "y" in r else "-x" if r[0] == d[0] else "+x"
	print(r)
	l = int(input())
