while True:
	try:
		print(" ".join([s[::-1] for s in input().split()]))
	except EOFError:
		break