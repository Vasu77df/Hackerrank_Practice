import sys 
def versionchecker(i_ver, j_ver):
    ver1 = [int(v) for v in i_ver.split(".")]
    ver2 = [int(v) for v in j_ver.split(".")]
    for i in range(max(len(ver1), len(ver2))):
        v1 = ver1[i] if i < len(ver1) else 0
        v2 = ver2[i] if i < len(ver2) else 0
        if v1>v2:
            return False
        elif v1 < v2:
            return True
          
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
            print(a)
            print(b)
            i_ver = a[1]
            j = b[0] # getting only yhe first portion
            j_ver = b[1]
            a = j.find(i)
            if a == -1:
                pass
            else:
              if versionchecker(i_ver, j_ver):
                count += 1
    print(count)
        
lists = []
for line in sys.stdin:
    lists.append(line.strip())

old, new = lists_gen(lists)
counter(old, new)
