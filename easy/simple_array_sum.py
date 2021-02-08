# https://www.hackerrank.com/challenges/simple-array-sum/problem

#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum = 0
    for e in ar:
        sum += e
        
    return sum
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()