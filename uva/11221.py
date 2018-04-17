stri = str
def magic(s, k):
	a, b = [], []
	c = s[::-1]
	if c != s:
		return False
	j = 0
	for i in range(k):
		a += c[j:j+k]
		b += [c[i+d*k] for d in range(k)]
		j += k
	return a == s and b == s

def main():
	for i in range(int(input())):
		s = list(input().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(' ', '').replace('(', '').replace(')', ''))
		k = len(s)**0.5
		if k.is_integer() and magic(s, int(k)):
			print("Case #" + stri(i+1) + ":\n" + stri(int(k)))
		else:
			print("Case #" + stri(i+1) + ":\nNo magic :(")

if __name__ == "__main__":
	main()
