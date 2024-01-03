from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:
    large = arr[0]
    for i in range(n):
        if large < arr[i]:
            large = arr[i]
    return large
