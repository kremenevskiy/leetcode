from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        return left if nums[left] == target else -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

nums = [-1,0,3,5,9,12]
target = 9
ans = 4
assert Solution().search(nums, target) == ans


nums = [-1,0,3,5,9,12]
target = 2
ans = -1
assert Solution().search(nums, target) == ans