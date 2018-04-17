s = input()
while s != "DONE":
	t = list(s.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(' ', '').lower())
	print("You won't be eaten!" if t == t[::-1] else "Uh oh..")
	s = input()
