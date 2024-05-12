class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx_sum = nums[0]
        cur_sum = 0
        for num in nums:
            if (num >= 0 or num > cur_sum) and cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            mx_sum = max(mx_sum, cur_sum)
        return mx_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = 6
assert Solution().maxSubArray(nums) == ans

nums = [1]
ans = 1
assert Solution().maxSubArray(nums) == ans

nums = [5,4,-1,7,8]
ans = 23
assert Solution().maxSubArray(nums) == ans


nums = [-2, -1]
ans = -1
assert Solution().maxSubArray(nums) == ans