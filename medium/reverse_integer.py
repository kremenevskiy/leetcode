class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_pos = x >= 0
        x = abs(x)
        if is_pos:
            return int(str(x)[::-1]) if -2**31 <= x <= 2**31 else 0
        return -int(str(x)[::-1]) if -2**31 <= x <= 2**31 else 0
    

x = 123
ans = 321
assert Solution().reverse(x) == ans

x = -123
ans = -321
assert Solution().reverse(x) == ans

x = 120
ans = 21
assert Solution().reverse(x) == ans