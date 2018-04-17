z = {'A': 'A', 'B': '0', 'C': '0', 'D': '0', 'E': '3', 'F': '0', 'G': '0', 'H': 'H', 'I': 'I', 'J': 'L', 'K': '0', 'L': 'J',
	 'M': 'M', 'N': '0', 'O': 'O', 'P': '0', 'Q': '0', 'R': '0', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
	 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '4': '0', '5': 'Z', '6': '0', '7': '0', '8': '8', '9': '9'}
x = ["is not a palindrome.", "is a regular palindrome.", "is a mirrored string.", "is a mirrored palindrome."]
def main():
	while True:
		try:
			s = list(input())
			i = int((len(s)+1)/2)
			t = [z[c] for c in s[:i]] + s[i:]
			c = False if len(s) & 1 and s[i-1] != t[i-1] else True
			a = 1 if s == s[::-1] else 0
			b = 2 if c and t == t[::-1] else 0
			print("".join(s) + " -- " + x[a+b] + "\n")
		except EOFError:
			break

if __name__ == "__main__":
	main()
