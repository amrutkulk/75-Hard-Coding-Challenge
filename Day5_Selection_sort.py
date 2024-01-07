from typing import List

def selectionSort(arr: List[int]) -> None: 

    for i in range(len(arr)):

        temp=i

        for j in range(i+1,len(arr)):

            if arr[j]<arr[temp]:

                temp=j 

        (arr[i],arr[temp]) = (arr[temp],arr[i])

    return arr