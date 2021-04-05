numbers = [4, 2, 1, 6 , 9, 7]

def square(x):
    return x*x

[square(x) for x in numbers]

def is_odd(x):
    return bool(x % 2)

list(filter(is_odd,numbers))

[x for x in numbers if is_odd(x)]


from collections import Counter
words = " if there was there was but if \
    there was not there was not".split()

counts = Counter(words)
print(counts)


