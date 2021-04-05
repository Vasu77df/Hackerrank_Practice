from collections import Counter

n =  int(input())
a = []
for i in range(n):
    a.append(input())

count = Counter(a)
l  = list(count.values())
print(len(l))
print(" ".join([str(x) for x in l]))


