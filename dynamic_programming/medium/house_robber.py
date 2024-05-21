class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, n):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])


class Solution:
    # how works?
    def rob(self, nums) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] 


nums = [1,3,5,100,1,1,300]
ans = 403
assert Solution().rob(nums) == ans

nums = [1,2,3,1]
ans = 4
assert Solution().rob(nums) == ans


nums = [2,7,9,3,1]
ans = 12
assert Solution().rob(nums) == ans