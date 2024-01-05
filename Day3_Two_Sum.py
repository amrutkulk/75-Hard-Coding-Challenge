#Approach1_Better_Hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i


#Approach2_Optimal

def read(n: int, book: [int], target: int) -> str:
    book = sorted(book)
    n = len(book)
    i, j = 0, n-1
    while(i<j):
        summ = book[i] + book[j]
        if summ == target:
            return "YES"
        elif summ > target:
            j-=1
        else:
            i+=1
    return "NO"