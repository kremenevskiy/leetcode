class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# solution with hash map O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        if len(s) != len(t):
            return False
        for ch in s:
            m[ch] = m.get(ch, 0) + 1
        for ch in t:
            if ch not in m or m[ch] == 0:
                return False
            m[ch] -= 1
        return True

s = "anagram"
t = "nagaram"
ans = True
assert Solution().isAnagram(s, t) == ans

s =  'rat'
t = 'car'
ans = False
assert Solution().isAnagram(s, t) == ans