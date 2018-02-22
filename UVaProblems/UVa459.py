from sys import stdin

par = []
set_size = 0


def initialize(size):
    global set_size
    set_size = size
    return [i for i in range(size)]


def find(i):
    return i if par[i] == i else find(par[i])


def union(a, b):
    if find(a) != find(b):
        par[find(a)] = find(b)
        global set_size
        set_size -= 1


t = int(input())
input()
for i in range(t):
    size = ord(input()) - ord('A') +1
    par = initialize(size)
    for line in stdin:
        if line == '\n':
            break
        else:
            union(ord(line[0])-65, ord(line[1])-65)
    print(set_size)
    print('')