import sys

def versionchecker(oldver, newver): # method to check which is the greater version
    ver1 = [int(v) for v in oldver.split(".")]
    ver2 = [int(v) for v in newver.split(".")]
    for i in range(max(len(ver1), len(ver2))):
        v1 = ver1[i] if i < len(ver1) else 0
        v2 = ver2[i] if i < len(ver2) else 0
        if v1>v2:
            return False
        elif v1 < v2:
            return True

def lists_gen(lists): # method to create separate lists for production and update
    index = lists[0].split(' ')
    x, y = index
    x = int(x)
    y = int(y)
    lists.pop(0)
    old = []
    new = []
    for i in range(x):
        old.append(lists[i])

    lists = lists[x:] # slice to start from the updates lists
    
    for i in range(y):
        new.append(lists[i])

    return old, new # list of the old softwares and the new ones

def counter(old, new):
    count = 0
    for i in old:
        a = i.split("-")
        i = a[0] # getting only the name portion
        oldver = a[1] # getting the version portion
        for j in new:
            #spliting strings
            b = j.split("-")
            j = b[0] # getting only the name portion
            newver = b[1] # getting only the verision portion
            x = j.find(i) # checking if the production version exists in updates list
            if x == -1:
                pass
            else:
                if versionchecker(oldver, newver): # checking if the updated version is newer or older
                    count += 1
    print(count)
        
lists = []
for line in sys.stdin:
    lists.append(line.strip())

old, new = lists_gen(lists)
counter(old, new)