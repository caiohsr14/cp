from sys import stdin, stdout
def nextPerm(s):
	i = len(s) - 1
	while i > 0 and s[i-1] >= s[i]:
		i -= 1
	if i <= 0:
		return False
	j = len(s) - 1
	while s[j] <= s[i-1]:
		j -= 1
	s[i-1], s[j] = s[j], s[i-1]
	s[i:] = s[len(s)-1:i-1:-1]
	return True

def main():
	for i in range(int(stdin.readline().strip())):
		s = list(stdin.readline().strip())
		s.sort()
		stdout.write(''.join(s) + "\n")
		if s != len(s) * s[0]:
			while nextPerm(s):
				stdout.write(''.join(s) + "\n")
			stdout.write("\n")

if __name__ == "__main__":
	main()
