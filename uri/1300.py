while True:
	try:
		print(int(input()) % 6 == 0 and 'Y' or 'N')
	except EOFError:
		break