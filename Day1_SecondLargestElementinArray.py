def secondlargest(arr, n):
    largest = arr[0]
    slargest = float('-inf')
    for i in range(n):
        if arr[i]>largest:
            slargest = largest
            largest = arr[i]
        elif arr[i]<largest and arr[i]>slargest:
            slargest = arr[i]
    return slargest

def secondsmallest(arr, n):
    smallest = arr[0]
    ssmallest = float('inf')
    for i in range(n):
        if arr[i]<smallest:
            ssmallest = smallest
            smallest = arr[i]
        elif arr[i]!=smallest and arr[i]<ssmallest:
            ssmallest = arr[i]
    return ssmallest
    

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    
    second_largest = secondlargest(a,n)
    second_smallest = secondsmallest(a,n)
    return second_largest, second_smallest
