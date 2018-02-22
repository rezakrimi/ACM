pset = [i for i in range(6)]


def find(i):
    return i if pset[i] == i else find(pset[i])


def union(i, j):
    pset[find(i)] = find(j)


def is_same(i, j):
    return find(i) == find(j)


def count():
    res = 0
    for i in range(6):
        res += 1 if i == pset[i] else 0
    return res

union(1,5)
union(5,3)
union(4,1)
union(0,1)
union(2,4)
print(count())