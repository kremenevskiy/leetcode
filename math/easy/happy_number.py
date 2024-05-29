class Solution:
    def isHappy(self, n: int) -> bool:
        prev_nums = set()
        while n not in prev_nums:
            prev_nums.add(n)
            n = sum([int(ch)**2 for ch in str(n)])
            if n == 1:
                return True
        return False

n = 19
ans = True
assert Solution().isHappy(n) == ans


n = 2
ans = False
assert Solution().isHappy(n) == ans