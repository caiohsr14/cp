#i think not solved
import sys
def solve(s, l, r, d):
	if abs(l-r) == 1:
		if s[r] and not s[l]:
			return s[r] + 1
		return 0
	if not s[r] and s[l]:
		print(l, r)
		return 0
	if d == 1:
		i = l+1 if l < r else l-1
		if not s[l]:
			return solve(s, r, i, 1)
		return solve(s, i, r, 1)
	elif d == 2:
		i = r-1 if r > l else r+1
		if not s[r]:
			print(l, r, i)
			return solve(s, i, l, 2)
		return solve(s, l, i, 2)
	if not s[r] and not s[l]:
		return solve(s, r, l+1, 1) + solve(s, r-1, l, 2)
	if not s[r]:
		return solve(s, l+1, r, 1) + solve(s, r-1, l, 2)
	if not s[l]:
		return solve(s, r, l+1, 1) + solve(s, l, r-1, 2)
	return solve(s, l+1, r, 1) + solve(s, l, r-1, 2)

def main():
	sys.setrecursionlimit(1500000)
	lol = ["a", "e", "i", "o", "u"]
	s = list(sys.stdin.readline().strip())
	p = []
	i = 0
	while i < len(s):
		f = 0
		if s[i] in lol:
			i += 1
		else:
			while i < len(s) and s[i] not in lol:
				f += 1
				i += 1
		p.append(f)
	print(p)
	if p.count(0) == 0 or p.count(0) == len(p):
		print(1)
	elif p[0] == 0 and p.count(0) == 1:
		print(len(s))
	else:
		print(solve(p, 0, len(p)-1, 0))

if __name__ == "__main__":
	main()
