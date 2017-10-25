s = [float(x) for x in input().split()]
while s[0] >= 0.0:
    z = 101 * [0.0]
    d = s[2] / s[0]
    m = 0
    for i in range(int(s[3])):
        a = input().split()
        z[int(a[0])] = float(a[1])
    c = s[1] + s[2] - (s[1] + s[2]) * z[0]
    while s[2] >= c:
        s[2] -= d
        m += 1
        z[0] = z[m] if z[m] != 0.0 else z[0]
        c -= c * z[0]
    print(m, "month" if m == 1 else "months")
    s = [float(x) for x in input().split()]
