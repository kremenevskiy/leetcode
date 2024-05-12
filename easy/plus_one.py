class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(x) for x in digits]
        int_num = [int(x) for x in str(int(''.join(digits)) + 1)]
        return int_num
        
        
digits = [1,2,3]
ans = [1,2,4]
assert Solution().plusOne(digits) == ans

digits = [4,3,2,1]
ans = [4,3,2,2]
assert Solution().plusOne(digits) == ans

digits = [9]
ans = [10]
assert Solution().plusOne(digits) == ans
        