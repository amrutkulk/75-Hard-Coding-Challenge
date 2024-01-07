#Approach1_BruteForce

def rearrange(arr, n):
    pos = []*(n/2)
    neg = []*(n/2)
    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    for i in range(len(pos)):
        arr[2*i] = pos[i]
    for i in range(len(neg)):
        arr[2*i+1] = neg[i]
    return arr

#Approach2_Optimal
from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    n = len(a)
    ans = [0]*n
    posi, negi = 0, 1
    for i in range(n):
        if a[i] < 0:
            ans[negi] = a[i]
            negi+=2
        else:
            ans[posi] = a[i]
            posi+=2
    return ans
