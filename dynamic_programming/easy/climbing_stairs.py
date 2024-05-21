class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        fib1, fib2 = 1, 2
        if n == 1:
            return fib1
        if n == 2:
            return fib2
        
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2

    

n = 2
ans = 2
assert Solution().climbStairs(n) == ans

n = 3
ans = 3
assert Solution().climbStairs(n) == ans


n = 4
ans = 5
assert Solution().climbStairs(n) == ans
        