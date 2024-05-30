class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n != 1:
            if n % 2 == 1:
                bits += 1
            n //= 2
        return bits + 1


class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            bits += n & 1
            n >>= 1
        return bits

n = 11
ans = 3
assert Solution().hammingWeight(n) == ans


n = 128
ans = 1
assert Solution().hammingWeight(n) == ans


n = 2147483645
ans = 30
assert Solution().hammingWeight(n) == ans