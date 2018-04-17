from sys import stdin, stdout
from functools import cmp_to_key

def topkek(x, y):
	if x != y:
		if x.lower() == y.lower():
			return 1 if x > y else -1
		return 1 if x.lower() > y.lower() else -1
	return 0

def nextPerm(s):
	i = len(s) - 1
	while i > 0 and topkek(s[i-1], s[i]) >= 0:
		i -= 1
	if i <= 0:
		return False
	j = len(s) - 1
	while topkek(s[j], s[i-1]) <= 0:
		j -= 1
	s[i-1], s[j] = s[j], s[i-1]
	s[i:] = s[len(s)-1:i-1:-1]
	return True


def main():
	for i in range(int(stdin.readline().strip())):
		s = list(stdin.readline().strip())
		if s == len(s) * s[0]:
			stdout.write(s)
		else:
			s.sort(key=cmp_to_key(topkek))
			stdout.write(''.join(s) + "\n")
			while nextPerm(s):
				stdout.write(''.join(s) + "\n")

if __name__ == "__main__":
	main()
