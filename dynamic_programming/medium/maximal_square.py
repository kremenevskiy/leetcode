import math
def show_matrix(matrix):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()

import math

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        mx_sq, cur_sq = 0, 0
        n, m = len(matrix), len(matrix[0])
        dp = [[int(matrix[i][j]) for j in range(m)]  for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if int(matrix[i][j]) > mx_sq:
                    mx_sq = int(matrix[i][j])
                if i > 0 and j > 0:
                    if matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1] == matrix[i][j] == "1":
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) * 4
                        cur_sq = (int(math.log(dp[i][j], 4) + 1)) ** 2
                        if cur_sq > mx_sq:
                            mx_sq = cur_sq
        return mx_sq

        
class Solution:
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
ans = 4
assert Solution().maximalSquare(matrix) == ans


matrix = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
ans = 16
assert Solution().maximalSquare(matrix) == ans


matrix = [[1]]
ans = 1
assert Solution().maximalSquare(matrix) == ans


matrix = [["0","1"],["1","0"]]
ans = 1
assert Solution().maximalSquare(matrix) == ans


matrix = [[0]]
ans = 0
assert Solution().maximalSquare(matrix) == ans

