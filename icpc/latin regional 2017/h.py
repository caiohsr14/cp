def main():
	c, b, p = [int(x) for x in input().split()]
	C, B, P = [int(x) for x in input().split()]
	s = 0
	s += C - c if C > c else 0
	s += B - b if B > b else 0
	s += P - p if P > p else 0
	print(s)

if __name__ == "__main__":
	main()
