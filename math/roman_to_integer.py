m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution(object):
    def romanToInt(self, s):
        prev = None
        ans = 0
        for idx, ch in enumerate(s):
            ch_int = m[ch]
            if prev and prev < ch_int:
                ans -= prev * 2
            ans += ch_int
            prev = ch_int
        return ans
    
print(Solution().romanToInt('III'))
assert Solution().romanToInt('III') == 3
assert Solution().romanToInt('LVIII') == 58
assert Solution().romanToInt('MCMXCIV') == 1994
