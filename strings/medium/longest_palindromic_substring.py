class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest = s[0]
        for i in range(1, len(s)):
            odd = expand(i-1, i)
            even = expand(i, i)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        return longest

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == s[::-1]:
            return s
        
        start, size = 1, 0
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l - 1:r], s[l:r]
            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size +  2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                
        return s[start:start + size]
    
        

        
s = "babad"
ans = "bab"
assert Solution().longestPalindrome(s) == ans

s = "cbbd"
ans = "bb"
assert Solution().longestPalindrome(s) == ans