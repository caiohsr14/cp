s = [float(x) for x in input().split()]
while s[0] >= 0.0:
    z = 101 * [0.0]
    t = s[2]
    d = t / s[0]
    m = 0
    for i in range(int(s[3])):
        a = input().split()
        z[int(a[0])] = float(a[1])
    p = z[0]
    c = s[2] + s[1]
    c -= c * p
    while t >= c:
        t -= d
        m += 1
        p = z[m] if z[m] != 0.0 else p
        c -= c * p
    print(m, "month" if m == 1 else "months")
    s = [float(x) for x in input().split()]
