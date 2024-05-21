class Solution:
    def tribonacci(self, n: int) -> int:
        t1, t2, t3 = 0, 1, 1
        if n == 0:
            return t1
        if n == 1:
            return t2
        if n == 2:
            return t3
        if n == 2:
            return t3
        for i in range(2, n):
            t1, t2, t3 = t2, t3, t1 + t2 + t3
        return t3

class Solution:
    def tribonacci(self, n: int) -> int:

        t0,t1,t2 = 0,1,1
        for i in range(n):
            t0,t1,t2 = t1,t2,(t0+t1+t2)

        return t0

n = 4
ans = 4
assert Solution().tribonacci(n) == ans


n = 25
ans = 1389537
assert Solution().tribonacci(n) == ans