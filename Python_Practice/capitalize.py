#!bin/python3

import math 
import os
import random
import re
import sys


def solve(s):
    # result = ''
    # word = ''
    # s_count = 0
    # space = ' '
    # for c in range(len(s)):
    #     if not s[c].isalnum():
    #         result += word.capitalize()
    #         word = ''
    #         s_count += 1
    #     else:
    #         result += space * s_count
    #         s_count = 0
    #         word += string[c]
    #         result += word.capitalize()
    #     return result
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    
    return s



if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT PATH'], 'w')

    s = input()

    result = solve(s)
    
    fptr.write(result +'\n')
    fptr.close()