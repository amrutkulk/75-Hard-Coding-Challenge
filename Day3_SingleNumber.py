from typing import *

def getSingleElement(arr : List[int]) -> int:
    n = len(arr)
    xorr = 0
    for i in range(n):
        xorr ^= arr[i]
    return xorr
   
