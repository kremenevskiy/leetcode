class Solution(object):
    def twoSum(self, nums, target):
        m = {}
        for idx, num in enumerate(nums):
            if target - num in m:
                return [m[target-num], idx]
            m[num] = idx
        return -1




assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
assert Solution().twoSum([3,2,4], 6) == [1, 2]
assert Solution().twoSum([3,3], 6) == [0, 1]