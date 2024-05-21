class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if sum(nums[i:j+1]) == k:
                    ans += 1
        return ans

from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        running = 0
        m = defaultdict(int)
        m[0] = 1
        for num in nums:
            running += num
            req = running - k
            if req in m:
                ans += m[req]
            m[running] += 1
        return ans
            



nums = [1,1,1]
k = 2
ans = 2
assert Solution().subarraySum(nums, k) == ans


nums = [1,1,1]
k = 2
ans = 2
assert Solution().subarraySum(nums, k) == ans
