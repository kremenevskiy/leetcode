class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans
        
nums = [2,2,1]
ans = 1
assert Solution().singleNumber(nums) == ans


nums = [4,1,2,1,2]
ans = 4
assert Solution().singleNumber(nums) == ans


nums = [1]
ans = 1
assert Solution().singleNumber(nums) == ans