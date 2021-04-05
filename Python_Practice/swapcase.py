def swap_case(s):
    # s = ''.join(c.lower() if c.isupper() else c.upper() for c in s)
    return s.swapcase()

if __name__ == '__main__':
    s= input()
    result = swap_case(s)
    print(result)