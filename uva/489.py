i = int(input())
while i != -1:
	print("Round", i)
	e = 0
	t = True
	s = set(list(input()))
	o = list(input())
	n = set()
	n_add = n.add
	o = [x for x in o if not (x in n or n_add(x))]
	for c in o:
		if c in s:
			s.remove(c)
		else:
			e += 1
		if not s:
			t = False
			print("You win.")
			break
		if e == 7:
			t = False
			print("You lose.")
			break
	if t:
		print("You chickened out.")
	i = int(input())
