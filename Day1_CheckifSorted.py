def isSorted(n: int,  a: [int]) -> int:
    for i in range(1,n):
        if a[i]>=a[i-1]:
            continue;
        else:
            return 0
    return 1
