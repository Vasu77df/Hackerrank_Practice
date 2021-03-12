import sys 
def lists_gen(lists):
    index = lists[0].split(' ')
    x, y = index
    x = int(x)
    y = int(y)
    lists.pop(0)
    old = []
    new = []
    for i in range(x):
        old.append(lists[i])

    lists = lists[x:]
    
    for i in range(y):
        new.append(lists[i])

    return old, new # list of the old softwares and the new ones

def counter(old, new):
    count = 0
    for i in old:
        for j in new:
            #spliting strings
            a = i.split("-")
            b = j.split("-")
            i = a[0] # getting only the first portion
            j = b[0] # getting only yhe first portion
            a = j.find(i)
            if a == -1:
                pass
            else:
                count += 1
    print(count)
        
lists = []
for line in sys.stdin:
    lists.append(line.strip())

old, new = lists_gen(lists)
counter(old, new)
    
