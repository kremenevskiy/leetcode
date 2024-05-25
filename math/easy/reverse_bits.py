class Solution:
    def reverseBits(self, n: int) -> int:
        s = [0] * 32
        ptr = 0
        while n >= 1:
            s[ptr] = n % 2
            n = n // 2
            ptr += 1
        
        res = 0
        for p, bit in enumerate(s[::-1]):
            res += bit * (2 ** p)
        return res


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res
    
n = 43261596
Solution().reverseBits(n)


n = 43261596
Solution().reverseBits(n)