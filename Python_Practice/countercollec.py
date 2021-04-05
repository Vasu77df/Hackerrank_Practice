from collections import Counter

x = int(input())

shoe = Counter(map(int, input().split()))
numCust = int(input())
income = 0
for i in range(numCust):
    size, price = map(int, input().split())
    if shoe[size]:
        income += price
        shoe[size] -= 1

print(income)
