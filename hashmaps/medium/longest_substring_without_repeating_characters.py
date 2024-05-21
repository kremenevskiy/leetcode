class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        left, prev = 0, s[0]
        longest = s[0]
        d = {s[0]: 0}
        r = 0

        for r in range(1, len(s)):
            if s[r] in d:
                if len(s[left:r]) > len(longest):
                    longest = s[left:r]
                tmp_left = left
                left = d[s[r]] + 1
 
                for ind in range(tmp_left, left):
                    del d[s[ind]]
            
            d[s[r]] = r

        return max(len(longest), len(s[left:r+1]))
    
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        used = {}
        start, mx_len = 0, 0

        for i, char in enumerate(s):
            
            if char in used:
                start = used[char] + 1
            else:
                mx_len = max(mx_len, i - start + 1)
            used[char] = i
        return mx_len



s = "abcabcbb"

ans = 3
assert Solution().lengthOfLongestSubstring(s) == ans


s = "bbbbb"
ans = 1
assert Solution().lengthOfLongestSubstring(s) == ans

s = "pwwkew"
ans = 3
assert Solution().lengthOfLongestSubstring(s) == ans

s = "abetkulez"
ans = 7
assert Solution().lengthOfLongestSubstring(s) == ans