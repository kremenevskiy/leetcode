class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        mx_len = 1
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] - nums[i-1] != 1:
                cur_len = 1
                continue
            cur_len += 1
            if cur_len > mx_len:
                mx_len = cur_len
        return mx_len


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        d = {}
        for num in nums:
            if num + 1 in d:
                d[num] = num + 1
            else:
                d[num] = num
        
        for k in d:
            if k + 1 in d:
                d[k] = k + 1
        
        mx_len = 1
        for k in d:
            cur_len = 1
            cur = k
            while cur + 1 in d:
                cur_len += 1
                cur += 1
            if cur_len > mx_len:
                mx_len = cur_len
        return mx_len


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        mx_len = 1
        nums_set = set(nums)
        cur_len = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                cur_len = 1
                while num + cur_len in nums_set:
                    cur_len += 1
                mx_len = max(mx_len, cur_len)
        return mx_len
                


nums = [100,4,200,1,3,2]
ans = 4
assert Solution().longestConsecutive(nums) == ans


nums = [0,3,7,2,5,8,4,6,0,1]
ans = 9
assert Solution().longestConsecutive(nums) == ans


nums = [0,-1]
ans = 2
assert Solution().longestConsecutive(nums) == ans