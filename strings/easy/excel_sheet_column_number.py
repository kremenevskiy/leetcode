class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n = len(columnTitle)
        for i in range(n):    
            res += 26 ** (i) * (ord(columnTitle[n-i-1]) - 64)
        return res

columnTitle = "A"
ans = 1
assert Solution().titleToNumber(columnTitle) == ans


columnTitle = "AA"
ans = 27
assert Solution().titleToNumber(columnTitle) == ans

columnTitle = "AB"
ans = 28
assert Solution().titleToNumber(columnTitle) == ans

columnTitle = "ZY"
ans = 701
assert Solution().titleToNumber(columnTitle) == ans