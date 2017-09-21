from collections import OrderedDict
s = input().split()
while (s[0] != "."):
	z = {}
	for word in s:
		if (len(word) > 2):
			if (word[0] not in z):
				z[word[0]] = word
			else:
				if ((len(z[word[0]])-2)*s.count(z[word[0]]) < (len(word)-2)*s.count(word)):
						z[word[0]] = word
	f = ""
	for word in s:
		if (word[0] in z and z[word[0]] == word):
			f += word[0] + ". "
		else:
			f += word + " "
	print (f[:-1])
	print (len(z))
	z = OrderedDict(sorted(z.items()))
	for k, v in z.items():
		print (k + ". = " + v)
	s = input().split()