#Approach1

def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n = len(arr)
    k = k % n
    temp = [0] * k
    for i in range(k):
        temp[i] = arr[i]
    
    for i in range(k,n):
        arr[i-k] = arr[i]
    
    for i in range(n-k,n):
        arr[i] = temp[i-(n-k)]
    return arr

#Approach2
def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n = len(arr)
    k = k % n
    arr[:k] = list(reversed(arr[:k]))
    arr[k:] = list(reversed(arr[k:]))
    arr = list(reversed(arr))
    return arr
