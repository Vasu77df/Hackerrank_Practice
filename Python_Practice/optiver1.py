import sys
# from collections import Counter

def duplicates(old):
    # seen = Counter(old)
    # seen = dict(seen)
    d = {}
    for i in old:
        d.setdefault(i, -1)
        d[i] += 1
        if d[i] >= 1:
            print("%s%d" % (i, d[i]))
        else:
            print(i)
          

lists = []
for line in sys.stdin:
    lists.append(line.strip('\n'))
    
duplicates(lists)


