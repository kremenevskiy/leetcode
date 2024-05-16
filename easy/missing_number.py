class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = n * (n+1) / 2
        ans = s - sum(nums)
        return ans
        


nums = [3, 0, 1]
ans = 2
assert Solution().missingNumber(nums) == ans

nums = [0, 1]
ans = 2
assert Solution().missingNumber(nums) == ans

nums = [9,6,4,2,3,5,7,0,1]
ans = 8
assert Solution().missingNumber(nums) == ans