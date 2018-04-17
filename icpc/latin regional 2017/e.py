def main():
	a = input().split()
	b = a[0]
	c = int(a[1])
	s = []
	d = 0
	t = b[-len(a[1])-1:].replace("?", "0")
	if t[0] == "0":
		t = "1" + t[1:]
	z = int(t) 
	x = c
	r = False
	while x < z:
		if z % x == 0:
			r = True
			break
		x += c
	if r:
		for i in range(len(b)):
			if b[i] != "?":
				s.append(i)
		i = 0
		while b[i] != "?":
			d = d*10 + int(b[i])
			i += 1
		d = d if d != 0 else 1
		e = d + 1
		idx = -1 if b[0] == "?" else len(b)
		e = e * 10**(len(b[b.find("?"):idx]))
		d = d * 10**(len(b[b.find("?"):idx]))
		g = d//c * c
		g = g if g >= d else g + c
		f = False
		while g < e:
			f = True
			for i in s:
				if str(g)[i] != b[i]:
					f = False
					break
			if f:
				break
			g += c
		if f:
			print(g)
		else:
			print("*")
	else:
		print("*")
if __name__ == "__main__":
	main()
