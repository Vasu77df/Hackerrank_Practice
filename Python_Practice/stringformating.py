val = int(input())

results = []

for i in range(1, val+1):
    dec = str(i)
    oc = str(oct(i)[2:])
    hex_ = str(hex(i)[2:]).upper()
    binary = str(bin(i)[2:])

    results.append([dec, oc, hex_, binary])

width = len(results[-1][3])

for i in results:
    print(*(rep.rjust(width)for rep in i))