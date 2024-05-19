class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = set([i for i in range(1, n+1)])
        return list(l^set(nums))


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
    


nums = [4,3,2,7,8,2,3,1]
ans = [5,6]
assert Solution().findDisappearedNumbers(nums) == ans


nums = [1,1]
ans = [2]
assert Solution().findDisappearedNumbers(nums) == ans
