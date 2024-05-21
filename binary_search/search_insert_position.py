class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while right - left > 1:
            mid = (right + left) // 2
            if target >= nums[mid]:
                left = mid
            else:
                right = mid
        
        if nums[left] == target:
            return left
        if nums[left] > target:
            return left
        return left if nums[left] >= target else left + 1



nums = [1,3,5,6]
target = 0
ans = 0
assert Solution().searchInsert(nums, target) == ans
    

nums = [1,3,5,6]
target = 5
ans = 2
assert Solution().searchInsert(nums, target) == ans


nums = [1,3,5,6]
target = 2
ans = 1
assert Solution().searchInsert(nums, target) == ans


nums = [1,3,5,6]
target = 7
ans = 4
assert Solution().searchInsert(nums, target) == ans