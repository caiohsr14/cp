N = 1000000
A = [0] * (N+1)
tree = [0] * (1048576<<1)
def setTree(l, r, k):
	if l == r:
		tree[k] = A[l]
	if l < r:
		m = (l+r) >> 1
		setTree(l, m, k<<1)
		setTree(m+1, r, (k<<1) + 1)
		tree[k] = max(tree[k<<1], tree[(k<<1)+1])

def getTree(l, r, k, i, j):
	if l == i and r == j:
		return tree[k]
	if l < r:
		m = (l+r) >> 1
		if m >= j:
			return getTree(l, m, k<<1, i, j)
		elif m < i:
			return getTree(m+1, r, (k<<1) + 1, i, j)
		else:
			return max(getTree(l, m, k<<1, i, m), getTree(m+1, r, (k<<1)+1, m+1, j))

def build():
	A[1] = 1
	for i in range(2, N+1):
		n = i
		ln = 1
		while n != 1:
			n = n*3 + 1 if n&1 else n>>1
			if n < N and A[n] != 0:
				ln += A[n]
				break
			ln += 1
		A[i] = ln
	setTree(1, N, 1)

build()
while True:
	try:
		i, j = [int(x) for x in input().split()]
		a = i if i < j else j
		b = i if i > j else j
		print (i, j, getTree(1, N, 1, a, b))
	except EOFError:
		break