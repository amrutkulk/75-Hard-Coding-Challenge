import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize-1 
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi