from sys import stdin

pset = []
set_size = 0


def initialize(size):
    global pset
    pset = [i for i in range(size)]
    global set_size
    set_size = size


def find(i):
    return i if pset[i] == i else find(pset[i])


def union(i, u):
    first = find(i)
    second = find(u)
    if first != second:
        global pset
        pset[first] = second
        global set_size
        set_size -= 1

t = int(input())
input()

for T in range(t):
    size = int(input())
    initialize(size)
    suc, unsuc = 0, 0

    while True:
        try:
            c, i, u = input().split(' ')
        except:
            break
        if c == 'c':
            union(int(i)-1, int(u)-1)
        else:
            if find(int(i)-1) == find(int(u)-1):
                suc += 1
            else:
                unsuc += 1

    print(','.join([str(suc),str(unsuc)]))
    if T != t-1:
        print()