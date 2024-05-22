from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res


num_rows = 5
ans = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert Solution().generate(num_rows) == ans


num_rows = 1
ans = [[1]]
assert Solution().generate(num_rows) == ans