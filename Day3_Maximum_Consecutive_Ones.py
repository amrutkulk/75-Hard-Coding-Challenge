class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cnt+=1
                maxi = max(cnt, maxi)
            else:
                cnt = 0
        return maxi
        