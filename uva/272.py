s = []
while True:
	try:
		s.append(input())
	except EOFError:
		l, r = "``", "''"
		rep = l
		for i in range(len(s)):
			while "\"" in s[i]:
				s[i] = s[i].replace("\"", rep, 1)
				rep = r if rep == l else l
		print ("\n".join(s))
		break