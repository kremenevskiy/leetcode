class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 3
        return x == n


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0

n = 27
ans = True
assert Solution().isPowerOfThree(n) == ans


n = 243
ans = True
assert Solution().isPowerOfThree(n) == ans

n = 0
ans = False
assert Solution().isPowerOfThree(n) == ans

n = -1
ans = False
assert Solution().isPowerOfThree(n) == ans