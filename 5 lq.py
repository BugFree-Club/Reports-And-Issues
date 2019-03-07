import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
        sum1=0
        sum2=0
        a=b=0
        while a<n:
            sum1+=arr[a][a]
            a+=1
        while b<n:
            sum2+=arr[b][n-b-1]
            b+=1
        return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()