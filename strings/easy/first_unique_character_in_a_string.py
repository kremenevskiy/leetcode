
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = defaultdict(int)
        for idx, ch in enumerate(s):
            store[ch] += 1
        for i in range(len(s)):
            if store[s[i]] == 1:
                return i
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        ptr = 0
        for idx, ch in enumerate(s):
            if ch not in store:
                store[ch] = 1
            else:
                store[ch] += 1

            
            while ptr < idx and store[s[ptr]] > 1:
                ptr += 1                
        return ptr if (ptr < len(s)) and (store[s[ptr]] == 1) else -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [0] * 26
        for i in range(1, len(s) + 1):
            ch_pos = ord(s[i-1]) - 97
            if arr[ch_pos] == 0:
                arr[ch_pos] = i
            else:
                arr[ch_pos] = -i
        
        min_ind = len(s) + 1
        for i in arr:
            if i > 0 and min_ind > i:
                min_ind = i
        
        return min_ind - 1 if min_ind != len(s) + 1 else -1

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, count in Counter(s).items():
            if count == 1:
                return s.find(i)

        return -1


s = "leetcode"
ans = 0
assert Solution().firstUniqChar(s) == ans

s = "loveleetcode"
ans = 2
assert Solution().firstUniqChar(s) == ans

s = "aabb"
ans = -1
assert Solution().firstUniqChar(s) == ans

s = "dddccdbba"
ans = 8
assert Solution().firstUniqChar(s) == ans