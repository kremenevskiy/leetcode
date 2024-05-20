from collections import defaultdict

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_earn = {}
        for n in nums:
            if n in num_earn:
                num_earn[n] += n
            else:
                num_earn[n] = n
        
        mx_val = max(list(num_earn.keys()))
        for i in range(mx_val):
            if i not in num_earn:
                num_earn[i] = 0

        sorted_earned = [val for _, val in sorted(num_earn.items(), key=lambda x: x[0], reverse=True)]

        mx_earned = 0
        prev1, prev2 = 0, 0
        for profit in sorted_earned:
            cur = max(prev1 + profit, prev2)
            prev1, prev2 = prev2, cur
            mx_earned = max(mx_earned, cur)
        return mx_earned

class Solution:
    def deleteAndEarn(self, nums) -> int:
        num_earn = {}
        num_earn = [0] * (max(nums) + 1)
        for n in nums:
            num_earn[n] += n
    

        mx_earned = 0
        prev1, prev2 = 0, 0
        for profit in num_earn:
            cur = max(prev1 + profit, prev2)
            prev1, prev2 = prev2, cur
            mx_earned = max(mx_earned, cur)
        return mx_earned


nums = [3, 1]
ans = 4
assert Solution().deleteAndEarn(nums) == ans


nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]
ans = 61
assert Solution().deleteAndEarn(nums) == ans

nums = [2,2,2,2]
ans = 8
assert Solution().deleteAndEarn(nums) == ans

nums = [3,4,2]
ans = 6
assert Solution().deleteAndEarn(nums) == ans

nums = [2,2,3,3,3,4]
ans = 9
assert Solution().deleteAndEarn(nums) == ans


# 1: 4  2: 6  3: 10   4:20

# 20, 10, 