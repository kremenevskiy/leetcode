class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x//2+1
        while left <= right:
            mid = (right + left) // 2
            if (mid * mid <= x) and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return left


x = 1
ans = 1
assert Solution().mySqrt(x) == ans

x = 0
ans = 0
assert Solution().mySqrt(x) == ans

x = 5
ans = 2
assert Solution().mySqrt(x) == ans

x = 4
ans = 2
assert Solution().mySqrt(x) == ans


x = 8
ans = 2
assert Solution().mySqrt(x) == ans


x = 63
ans = 7
assert Solution().mySqrt(x) == ans


x = 100
ans = 10
assert Solution().mySqrt(x) == ans


x = 82
ans = 9
assert Solution().mySqrt(x) == ans