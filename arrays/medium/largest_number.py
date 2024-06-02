from typing import List

def compare(num1: str, num2 : str):
    if len(num1) == len(num2):
        return int(num1) - int(num2)
    else:
        num1, num2 = num1 + num2, num2 + num1
        return int(num1) - int(num2)
    
    
def compare(num1: str, num2 : str):
    if len(num1) == len(num2):
        return int(num1) - int(num2)
    else:
        if num1 * 9 > num2 * 9:
            return 1
        else:
            return -1
        
            
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(n == 0 for n in nums):
            return "0"
        nums = sorted([str(num) for num in nums], key=cmp_to_key(compare), reverse=True)
        ans =  ''.join(nums)
        return ans

nums = [10, 2]
ans = "210"
assert Solution().largestNumber(nums) == ans


nums = [3,30,34,5,9]
ans = "9534330"
assert Solution().largestNumber(nums) == ans


nums = [34323,3432]
ans = "343234323"
assert Solution().largestNumber(nums) == ans

nums = [0, 0]
ans = "0"
assert Solution().largestNumber(nums) == ans
