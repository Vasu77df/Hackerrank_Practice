from itertools import product 

k, n = [int(x) for x in input().split()]

L = []
for _ in range(k):
    L.append([int(x) for x in input().split()[1:]])

best = 0
for c in product(*L):
    s = sum([x * x for x in c]) % n
    best = max(best, s)

print(best)
