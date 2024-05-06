class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        min_len_work = len(min(strs, key=len))
        for i in range(min_len_work):
            letts = {s[i] for s in strs}
            if len(letts) != 1:
                return ans
            
            ans += letts.pop()
        return ans


class Solution(object):
    def longestCommonPrefix(self, strs):
        strs = sorted(strs)
        
        first = strs[0]
        last = strs[-1]
        idx = 0
        for i in range(len(first)):
            if first[i] == last[i]:
                idx += 1
            else:
                break
        return first[:idx]
                
        


Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
Solution().longestCommonPrefix(["dog","racecar","car"]) == ""