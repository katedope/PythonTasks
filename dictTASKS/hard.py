def s(a):
    d = []
    p = 0
    r = int(input())
    for i in range(0, len(a)):
        d.append(a[i][2])
        for y in range(0, len(d)):
            while p != d[y+r + 2]:
            p = d[y]


