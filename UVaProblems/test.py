def _find(x):
    if dset[x] < 0:
        return x
    else:
        dset[x] = _find(dset[x])
        return dset[x]


def _union(x, y):
    a = _find(x)
    b = _find(y)
    if a == b:
        return
    if dset[a] > dset[b]:
        a, b = b, a
    dset[a] += dset[b]
    dset[b] = a


T = int(input())
input()
for t in range(T):
    N = int(input())
    us = 0
    s = 0
    dset = [-1] * (N + 1)
    while True:
        try:
            c, u, v = input().split()
        except Exception:
            break
        u = int(u)
        v = int(v)
        if c == 'c':
            _union(u, v)
        else:
            if _find(u) != _find(v):
                us += 1
            else:
                s += 1
    print(str(s) + ',' + str(us))
    if t != T - 1:
        print()