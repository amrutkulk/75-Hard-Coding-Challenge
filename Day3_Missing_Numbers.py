#Approach1_BruteForce

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0]*(n+1)
        for i in range(n):
            a[nums[i]] = 1
        for i in range(n+1):
            if a[i] == 0:
                return i

#Approach2_Optimal_Solution
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0]*(n+1)
        for i in range(n):
            a[nums[i]] = 1
        for i in range(n+1):
            if a[i] == 0:
                return i