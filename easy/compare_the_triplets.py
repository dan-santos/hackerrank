# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    output_a = output_b = 0
    for i, x in enumerate(a):
        if x > b[i]: 
            output_a += 1
        elif x < b[i]:
            output_b += 1
    
    return output_a, output_b


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

    '''fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()'''
