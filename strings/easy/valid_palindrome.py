class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ch for ch in s.lower() if ch.isalnum()])
        return s == s[::-1]


s = "A man, a plan, a canal: Panama"
ans = True
assert Solution().isPalindrome(s) == ans

s = " "
ans = True
assert Solution().isPalindrome(s) == ans

s = "race a car"
ans = False
assert Solution().isPalindrome(s) == ans