from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, 0
        min_cost = 0
        for cur_cost in cost:
            prev1, prev2 = prev2, min(prev2, prev1) + cur_cost
        return min(prev1, prev2)


cost = [10, 15, 20]
ans = 15
assert Solution().minCostClimbingStairs(cost) == ans


cost = [1,100,1,1,1,100,1,1,100,1]
ans = 6
assert Solution().minCostClimbingStairs(cost) == ans