from collections import OrderedDict
while True:
	try:
		cards = input().split()
		p, b, m = 0, 0, -1
		bd = "topkek"
		w = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}
		st = OrderedDict([('S', 0), ('H', 0), ('D', 0), ('C', 0)])
		z = {'AS': 0, 'KS': 0, 'QS': 0, 'JS': 0, 'AH': 0, 'KH': 0, 'QH': 0, 'JH': 0, 'AD': 0, 'KD': 0, 'QD': 0, 'JD': 0, 'AC': 0, 'KC': 0, 'QC': 0, 'JC': 0}
		for c in cards:
			p += w[c[0]] if c[0] in w else 0
			st[c[1]] += 1
			if c in z:
				z[c] += 1
		for k, v in st.items():
			p -= 1 if z['K' + k] and v < 2 else 0
			p -= 1 if z['Q' + k] and v < 3 else 0
			p -= 1 if z['J' + k] and v < 4 else 0
			b += 1 if v == 2 else 2 if v < 2 else 0
			bd = k if v > m else bd
			m = v if v > m else m
		s = True if z['AS'] or (z['KS'] and st['S'] > 1) or (z['QS'] and st['S'] > 2) else False
		h = True if z['AH'] or (z['KH'] and st['H'] > 1) or (z['QH'] and st['H'] > 2) else False
		d = True if z['AD'] or (z['KD'] and st['D'] > 1) or (z['QD'] and st['D'] > 2) else False
		c = True if z['AC'] or (z['KC'] and st['C'] > 1) or (z['QC'] and st['C'] > 2) else False
		if p > 15 and s and h and d and c:
			print("BID NO-TRUMP")
		elif p + b > 13:
			print ("BID", bd)
		else:
			print ("PASS")
	except EOFError:
		break
