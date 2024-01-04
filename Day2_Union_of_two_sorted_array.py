def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    i, j = 0, 0 
    union = []
    
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1
        else:  # a[i] == b[j]
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
            j += 1
        
    while i < len(a):
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1
        
    while j < len(b):    
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    
    return union
