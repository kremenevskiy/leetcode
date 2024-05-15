class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = set()
        for num in nums:
            if num in m:
                return True
            m.add(num)
        return False
        


nums = [1,2,3,1]
ans = True
assert Solution().containsDuplicate(nums) == ans


nums = [1,2,3,4]
ans = False
assert Solution().containsDuplicate(nums) == ans


nums = [1,1,1,3,3,4,3,2,4,2]
ans = True
assert Solution().containsDuplicate(nums) == ans