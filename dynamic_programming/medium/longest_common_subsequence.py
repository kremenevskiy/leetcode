class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                dp[i+1][j+1] = dp[i][j] + 1 if text1[i] == text2[j] else max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        if m < n:
            tex1, tex2 = text2, text1
        dp = [0] * (n + 1)
        for c in text1:
            prevRow, prevRowPrevCol = 0, 0
            for j, d in enumerate(text2):
                prevRow, prevRowPrevCol = dp[j + 1], prevRow
                dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
        return dp[-1]

text1 = 'abcde'
text2 = 'ace'
ans = 3
assert Solution().longestCommonSubsequence(text1, text2) == ans

text1 = 'abc'
text2 = 'abc'
ans = 3
assert Solution().longestCommonSubsequence(text1, text2) == ans


text1 = 'abc'
text2 = 'def'
ans = 0
assert Solution().longestCommonSubsequence(text1, text2) == ans